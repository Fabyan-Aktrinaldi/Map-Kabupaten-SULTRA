import geopandas as gpd

# 1. Baca file desa se-Indonesia
gdf = gpd.read_file("geojson.json")

# 2. Ambil hanya Sulawesi Tenggara, buang baris tanpa geometri
gdf = gdf[gdf["WADMPR"] == "Sulawesi Tenggara"]
gdf = gdf[gdf.geometry.notna()]

# 3. Gabungkan semua desa yang punya WADMKK sama jadi satu polygon
kab = gdf.dissolve(by="WADMKK", as_index=False)[["WADMKK", "geometry"]]

# 4. Samakan nama dengan kolom Wilayah di Metabase
kab["name"] = kab["WADMKK"].replace({
    "Kota Bau Bau": "Baubau",
    "Kota Kendari": "Kendari",
})

# 5. Simpan hanya kolom name + geometry
kab[["name", "geometry"]].to_file("sultra_kabkota.geojson", driver="GeoJSON")

print(sorted(kab["name"].tolist()))