# nxc_lead_qualification

This custom module was developed for Next Chapter Manufacturing to enable tracking of on-time deliveries.

## Features
- Creates a new field in the stock.picking model titled 'Completed On Time'.
- Computes the value of this field based on the deadline and effective date fields.

## Installation
To install this module, you can use the following steps:

1. Copy this directory to addons folder.
2. Allow Odoo server to restart.
3. Go to Apps.
4. Click 'update apps list' button.
5. Clear search filter and search for this addon.
6. Click Install.

## Usage
To use this module, you can follow these steps:

1. Go to Inventory > Delivery Orders.
2. Click Create.
4. 'Completed On Time' field will be computed (Note: This only applies if the deadline field is set).

## Support
If you have any questions or problems with this module, please contact the author at haydenmccarthy19@gmail.com