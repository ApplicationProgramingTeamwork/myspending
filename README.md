# My Spending
A web application designed to track supermarket expenses. It automatically captures product information by scanning supermarket receipts, helping you with expense tracking, analyzing your spending patterns, and offering additional features to manage your finances efficiently.

## TODO
Here are the tasks we need to do.

### Models
- [ ] Receipt: `storeName`, `storeAddress`, `totalPrice`, `date`
- [ ] ReceiptProduct: `receipt`, `name`, `nameEnglish`, `nameChinese`, `price`, `discount`

### views
- [ ] Receipt List View: Display a list of all receipts with basic details like store name, date, and total price.
- [ ] Receipt Detail View: Display detailed information of a selected receipt, including all products, their prices, and any discounts applied.
- [ ] Add Receipt View: A form to add a new receipt manually, including fields for store name, store address, total price, and date.
- [ ] Edit Receipt View: A form to edit an existing receipt's details.

### URLs
- [ ] `/receipts/`: URL to view the list of receipts.
- [ ] `/receipts/<id>/`: URL to view the details of a specific receipt.
- [ ] `/receipts/add/`: URL to add a new receipt.
- [ ] `/receipts/<id>/edit/`: URL to edit an existing receipt.

## Receipt example and its recognized data
![这是图片](/readme/example4.jpeg)

```json
{
  "storeName": "Lidl",
  "storeAddress": "Lidl Suomi Ky Turku-Keskusta Eerikinkatu 4",
  "items": [
    {
      "name": "Rostin Bao Bun höyry­sämpy­lä",
      "nameEnglish": "Steamed Bao Bun",
      "nameChinese": "蒸笼包",
      "price": 2.39,
      "discount": 0.29
    },
    {
      "name": "Pizza vega­ta­ria­na",
      "nameEnglish": "Vegetarian Pizza",
      "nameChinese": "素食披萨",
      "price": 1.44,
      "discount": 0
    },
    {
      "name": "2 x 2,39",
      "nameEnglish": "2 x 2.39",
      "nameChinese": "2 x 2.39",
      "price": 0,
      "discount": -1.39
    },
    {
      "name": "ALENNUS",
      "nameEnglish": "Discount",
      "nameChinese": "折扣",
      "price": 0,
      "discount": -1.39
    },
    {
      "name": "Lidl Plus -säästösi",
      "nameEnglish": "Lidl Plus Savings",
      "nameChinese": "Lidl Plus 优惠",
      "price": 0,
      "discount": -1.09
    },
    {
      "name": "Juustokierre",
      "nameEnglish": "Cheese Roll",
      "nameChinese": "芝士卷",
      "price": 0,
      "discount": -0.85
    },
    {
      "name": "Lidl Plus -säästösi",
      "nameEnglish": "Lidl Plus Savings",
      "nameChinese": "Lidl Plus 优惠",
      "price": 0,
      "discount": -0.85
    },
    {
      "name": "Peruna yleis 4kg",
      "nameEnglish": "General Potatoes 4kg",
      "nameChinese": "普通土豆 4kg",
      "price": 3.39,
      "discount": 0
    },
    {
      "name": "Harvest Basket ranskanperuna",
      "nameEnglish": "Harvest Basket French Fries",
      "nameChinese": "收获篮薯条",
      "price": 1.39,
      "discount": 0
    },
    {
      "name": "Ocean Sea MSC Kalapullikot 18K",
      "nameEnglish": "Ocean Sea MSC Fish Fillets 18K",
      "nameChinese": "海洋之海 MSC 鱼片 18K",
      "price": 2.15,
      "discount": 0
    },
    {
      "name": "Munax Vapaan kanan kananmuna",
      "nameEnglish": "Free-Range Chicken Eggs",
      "nameChinese": "自由放养鸡鸡蛋",
      "price": 2.69,
      "discount": 0
    }
  ],
  "totalPrice": 12.96,
  "date": "2024-09-28T17:02:00Z"
}
```