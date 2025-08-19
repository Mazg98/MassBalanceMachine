# <------------------ INAMHI/Local Glacier Data: ------------------>
# Point data
path_PMB_INAMHI_raw = '../../../data/INAMHI/point/raw/'
path_PMB_INAMHI_csv = '../../../data/INAMHI/point/csv/'

# Glacier wide data
path_SMB_INAMHI_raw = '../../../data/INAMHI/glacier-wide/raw/'
path_SMB_INAMHI_csv = '../../../data/INAMHI/glacier-wide/csv/'

# Gridded data for MBM to use for making predictions over whole grid
path_glacier_grid = '../../../data/INAMHI/topo/gridded_topo_inputs/'  # DEMs & topo

# Topo data
path_DEM = '../../../data/INAMHI/topo/DEM/'  # DEMs
path_pcsr = '../../../data/INAMHI/topo/pcsr/'  # Potential incoming clear sky solar radiation

path_distributed_MB = '../../../data/INAMHI/distributed_MB_grids/'
path_geodetic_MB = '../../../data/INAMHI/geodetic/'
path_glacier_ids = '../../../data/INAMHI/EC_glacier_ids.csv'  # glacier ids for EC glaciers

# <------------------ OTHER PATHS: ------------------>
path_ERA5_raw = '../../../data/ERA5Land/raw/'  # ERA5-Land
path_S2 = '../../../data/Sentinel/'  # Sentinel-2
path_OGGM = '../../../data/OGGM/'
path_glogem = '../../../data/GloGEM'  # glogem c_prec and t_off factors

# <------------------ OTHER USEFUL FUNCTIONS & ATTRIBUTES: ------------------>
vois_climate_long_name = {
    't2m': 'Temperature',
    'tp': 'Precipitation',
    't2m_corr': 'Temperature corr.',
    'tp_corr': 'Precipitation corr.',
    'slhf': 'Surf. latent heat flux',
    'sshf': 'Surf. sensible heat flux',
    'ssrd': 'Surf. solar rad. down.',
    'fal': 'Albedo',
    'str': 'Surf. net thermal rad.',
    'pcsr': 'Pot. in. clear sky solar rad.',
    'u10': '10m E wind',
    'v10': '10m N wind',
}

vois_units = {
    't2m': 'C',
    'tp': 'm w.e.',
    't2m_corr': 'C',
    'tp_corr': 'm w.e.',
    'slhf': 'J m-2',
    'sshf': 'J m-2',
    'ssrd': 'J m-2',
    'fal': '',
    'str': 'J m-2',
    'pcsr': 'J m-2',
    'u10': 'm s-1',
    'v10': 'm s-1',
}
