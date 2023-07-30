import csv
from qrcode import make as make_qr_code

#defines fixed assets
class FixedAsset:
    def __init__(self, asset_id, name, asset_type, acquisition_date, original_cost, useful_life, depreciation_per_month):
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.acquisition_date = acquisition_date
        self.original_cost = original_cost
        self.useful_life = useful_life
        self.depreciation_per_month = depreciation_per_month

    def generate_qr_code (self):
        qr_data = f"Asset ID: {self.asset_id}\nAsset Name: {self.name}\nAssetType: {self.asset_type}\nAcquisition Date: {self.acquisition_date}\nOriginal Cost: {self.original_cost}\nUseful life: {self.useful_life}n\nDepreciation per month: {self.depreciation_per_month}"
        qr = make_qr_code(qr_data)
        qr.save(f"{self.asset_id}_qr_code.png")

#Reads fixed asset data from CSV and create FixedAsset objects
fixed_assets = []
with open('FA_simulated_07.26.23.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        asset_id = row['Asset ID']
        name = row['Asset Name']
        asset_type = row['Asset Type']
        acquisition_date = row['Acquisition Date']
        original_cost = row['Original Cost']
        useful_life = row['Useful life']
        depreciation_per_month = row['Depreciation per month']
        asset = FixedAsset(asset_id, name, asset_type, acquisition_date, original_cost, useful_life, depreciation_per_month)
        fixed_assets.append(asset)


#Generate QR codes for each fixed asset
for asset in fixed_assets:
    asset.generate_qr_code()