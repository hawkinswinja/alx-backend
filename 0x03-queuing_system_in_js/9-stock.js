import express from 'express';
import { promisify } from 'util';
import redis from 'redis';

const client = redis.createClient();
const app = express();

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
	{ Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];


const data = [{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},{"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},{"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},{"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}];

function getItemById(id) {
  for (const item of listProducts) {
    if (item.Id === id)
      return item;
  }
};

function reserveStockById(itemid, stock) {
  const item = getItemById(itemid)
  if (item) 
	  client.set(itemid, stock);
};

const get = promisify(client.get).bind(client);

async function getCurrentReservedStockById(itemid) {
  const val = await get(itemid);
  if (val === null)
    return 0;
  return val;
};

app.get('/list_products', (req, res) => {
  res.status(200).json(data);
});

app.get('/list_products/:itemid', (req, res) => {
  const id = Number(req.params.itemid);
  const item = getItemById(id);
  if (item) {
    getCurrentReservedStockById(id).then((r) => {
      const data = {
        "itemId":item.Id,
        "itemName":item.name,
			  "price":item.price,
			  "initialAvailableQuantity":item.stock,
			  "currentQuantity":item.stock - r,
      };
      res.json(data);
    }).catch ((e) => res.end(e.message));
	}	else {
    res.status(404).json({"status":"Product not found"});
	}
});

app.get('/reserve_product/:itemId', (req, res) => {
  const id = Number(req.params.itemId);
  const item = getItemById(id);
  if (item) {
    getCurrentReservedStockById(id).then((r) => {
      if (item.stock - r < 1)
	      res.json({"status":"Not enough stock available","itemId":1});
      reserveStockById(id, 1);
	    res.json({"status":"Reservation confirmed","itemId":1});
    });
  } else { 
  res.json({"status":"Product not found"});
  }
});

app.listen(1245, () => console.log('listening on port 1245'));
