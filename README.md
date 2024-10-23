# My Spending
A web application designed to track supermarket expenses. It automatically captures shopping details by taking a photo of the receipt, helping you monitor your spending, analyze your purchasing habits, and offering additional features to efficiently manage your finances.

## Install
You need to run the following command when you first install this project
```shell
pip install -r requirements.txt
```

Then, create a `.env` file in the root directory with the following content
```shell
# Apply Gemini API keys at https://ai.google.dev
GEMINI_API_KEY="" 
DATABASE_URL="postgresql://username:password@localhost:5432/myspending"
```

## TODO
Here are the tasks we need to do.

### Feature
- [x] AI: Upload the photo to the AI server and analyze the receipt’s contents.
- [x] Receipt List Page: View previously analyzed receipts.
- [x] Receipt Detail Page: Access details from the receipt list to see the shopping information captured from the receipt.
- [x] Receipt Edit Page: Edit the receipt’s content. Since the AI’s accuracy isn’t 100%, manual adjustments may be necessary.
- [ ] Financial Analysis Page: Analyze data visually, such as monthly spending, preferred supermarkets, discount comparisons, and more.

### Models
- [x] Receipt: `storeName`, `storeAddress`, `totalPrice`, `date`
- [x] Product: `receipt`, `name`, `nameEnglish`, `nameChinese`, `price`, `discount`

### views
- [x] Photo upload view: Upload a photo to the AI
- [x] Receipt List View: Display a list of all receipts with basic details like store name, date, and total price.
- [x] Receipt Detail View: Display detailed information of a selected receipt, including all products, their prices, and any discounts applied.
- [x] Add Receipt View: A form to add a new receipt manually, including fields for store name, store address, total price, and date.
- [ ] Edit Receipt View: A form to edit an existing receipt's details.

### URLs
- [x] `/ai/upload_photo`: Upload a photo to the AI.
- [x] `/receipts/`: URL to view the list of receipts.
- [x] `/receipts/<receipts_id>/`: URL to view the details of a specific receipt.
- [x] `/receipts/add/`: URL to add a new receipt.
- [ ] `/receipts/<receipts_id>/product/<product_id>/edit`: URL to edit the details of a specific product in a receipt.

## Receipt example and its recognized data
![example](/readme/example.jpeg)

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

