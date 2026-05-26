# BizAxl Assets

Asset Management for BizAxl ERP.

## Requires
- bizaxl_erp

## DocTypes
- BA Asset (with depreciation schedule)
- BA Asset Category, BA Asset Movement
- BA Asset Maintenance, BA Asset Repair

## Installation
```bash
bench get-app https://github.com/kevin-kuriakose/bizaxl-assets.git
bench --site yoursite install-app bizaxl_assets
bench --site yoursite migrate
```
