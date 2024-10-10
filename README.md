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