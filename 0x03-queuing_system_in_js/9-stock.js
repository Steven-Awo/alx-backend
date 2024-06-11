#!/usr/bin/yarn dev
import express from 'express';

import { createClient } from 'redis';

import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  },
];

const getItemById = (id) => {

  const item = listProducts.find(obj => obj.itemId === id);

  if (item) {

    return Object.fromEntries(Object.entries(item));

  }

};

const app = express();

const client = createClient();

const PORT = 1245;

/**
 * Modifies just the reserved stock thats for the given item.
 * @param {number} itemId - The items id.
 * @param {number} stock - The item's stock.
 */

const reserveStockById = async (itemId, stock) => {

  return promisify(client.SET).bind(client)(`item.${itemId}`, stock);

};

/**
 * Retrieves just the reserved stock thats for the given item..
 * @param {number} itemId - The item's id.
 * @returns {Promise<String>}
 */

const getCurrentReservedStockById = async (itemId) => {

  return promisify(client.GET).bind(client)(`item.${itemId}`);

};

app.get('/list_products', (_, res) => {

  res.json(listProducts);

});

app.get('/list_products/:itemId(\\d+)', (req, res) => {

  const itemId = Number.parseInt(req.params.itemId);

  const product_Item = getItemById(Number.parseInt(itemId));

  if (!product_Item) {

    res.json({ status: 'Product not found' });

    return;

  }

  getCurrentReservedStockById(itemId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {

      product_Item.currentQuantity = product_Item.initialAvailableQuantity - reservedStock;

      res.json(product_Item);

    });

});

app.get('/reserve_product/:itemId', (req, res) => {

  const itemId = Number.parseInt(req.params.itemId);

  const product_Item = getItemById(Number.parseInt(itemId));

  if (!product_Item) {

    res.json({ status: 'Product not found' });

    return;

  }

  getCurrentReservedStockById(itemId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {

      if (reservedStock >= product_Item.initialAvailableQuantity) {

        res.json({ status: 'Not enough stock available', itemId });

        return;

      }

      reserveStockById(itemId, reservedStock + 1)
        .then(() => {

          res.json({ status: 'Reservation confirmed', itemId });

        });
    });
});

const resetint_Products_Stock = () => {

  return Promise.all(
    listProducts.map(
      item => promisify(client.SET).bind(client)(`item.${item.itemId}`, 0),
    )
  );

};

app.listen(PORT, () => {

  resetint_Products_Stock()
    .then(() => {

      console.log(`API available on localhost port ${PORT}`);

    });
});

export default app;
