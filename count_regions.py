from awag.views import REGIONS_58
print(f'Total: {len(REGIONS_58)}')
for i, r in enumerate(REGIONS_58):
    print(f"{i+1}. {r['code']} - {r['name']} - {r['wind']} - {r['rain']}")