# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_13:53:24_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-06-23 13:53:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-23 13:53:24 UTC

- **117,636** saved flights
- **40,611** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **117,636** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,427,440.0 tonnes** estimated CO2 emissions
- **82,750,142 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4851 |
| 2 | SkyWest Airlines | 4353 |
| 3 | IndiGo | 2275 |
| 4 | EJA | 2270 |
| 5 | American Airlines | 1833 |
| 6 | Southwest Airlines | 1753 |
| 7 | ENY | 1468 |
| 8 | Delta Air Lines | 1385 |
| 9 | Lufthansa | 1298 |
| 10 | Vueling | 1063 |
| 11 | LATAM Airlines | 1042 |
| 12 | WIF | 1037 |
| 13 | AZU | 982 |
| 14 | AXM | 969 |
| 15 | LXJ | 894 |
| 16 | Swiss International | 831 |
| 17 | All Nippon Airways | 811 |
| 18 | Alaska Airlines | 781 |
| 19 | QLK | 759 |
| 20 | easyJet | 750 |
| 21 | EJU | 735 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 659 |
| 24 | VIV | 649 |
| 25 | Air France | 646 |
| 26 | United Airlines | 645 |
| 27 | CXK | 630 |
| 28 | MXY | 620 |
| 29 | AXB | 582 |
| 30 | GLO | 576 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 99332 |
| 2 | 🇪🇸 ES | 8030 |
| 3 | 🇮🇳 IN | 7153 |
| 4 | 🇦🇺 AU | 6980 |
| 5 | 🇧🇷 BR | 6494 |
| 6 | 🇮🇹 IT | 6285 |
| 7 | 🇩🇪 DE | 6274 |
| 8 | 🇨🇦 CA | 6155 |
| 9 | 🇯🇵 JP | 5294 |
| 10 | 🇬🇧 GB | 5146 |
| 11 | 🇫🇷 FR | 4689 |
| 12 | 🇨🇴 CO | 3996 |
| 13 | 🇲🇽 MX | 3457 |
| 14 | 🇬🇷 GR | 3362 |
| 15 | 🇳🇴 NO | 3229 |
| 16 | 🇨🇭 CH | 3020 |
| 17 | 🇲🇾 MY | 2518 |
| 18 | 🇹🇷 TR | 2399 |
| 19 | 🇿🇦 ZA | 1979 |
| 20 | 🇵🇱 PL | 1931 |
| 21 | 🇳🇿 NZ | 1921 |
| 22 | 🇹🇭 TH | 1899 |
| 23 | 🇰🇷 KR | 1896 |
| 24 | 🇵🇭 PH | 1706 |
| 25 | 🇬🇹 GT | 1659 |
| 26 | 🇲🇦 MA | 1276 |
| 27 | 🇲🇴 MO | 1170 |
| 28 | 🇲🇪 ME | 1165 |
| 29 | 🇳🇱 NL | 1133 |
| 30 | 🇭🇷 HR | 1023 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2478 |
| 2 | Denver International Airport |  | US | 1979 |
| 3 | Tokyo International Airport |  | JP | 1754 |
| 4 | Indira Gandhi International Airport |  | IN | 1570 |
| 5 | Guaymaral Airport |  | CO | 1486 |
| 6 | Harry Reid International Airport |  | US | 1467 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1434 |
| 8 | Zurich Airport |  | CH | 1314 |
| 9 | La Aurora Airport |  | GT | 1281 |
| 10 | Frankfurt am Main International Airport |  | DE | 1260 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1246 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1170 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1166 |
| 15 | Chicago O'Hare International Airport |  | US | 1151 |
| 16 | Capua Airport |  | IT | 1017 |
| 17 | Salt Lake City International Airport |  | US | 1008 |
| 18 | Madrid Barajas International Airport |  | ES | 993 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 981 |
| 20 | Kuala Lumpur International Airport |  | MY | 974 |
| 21 | Congonhas Airport |  | BR | 905 |
| 22 | Charlotte/Douglas International Airport |  | US | 894 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 878 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 878 |
| 25 | Charles de Gaulle International Airport |  | FR | 865 |
| 26 | Bengaluru International Airport |  | IN | 865 |
| 27 | Malpensa International Airport |  | IT | 832 |
| 28 | Ninoy Aquino International Airport |  | PH | 788 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 772 |
| 30 | Daniel K Inouye International Airport |  | US | 762 |
| 31 | Tenerife Norte Airport |  | ES | 759 |
| 32 | Barcelona International Airport |  | ES | 748 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Vitoria/Foronda Airport |  | ES | 690 |
| 35 | Calgary International Airport |  | CA | 688 |
| 36 | Amsterdam Airport Schiphol |  | NL | 688 |
| 37 | Don Mueang International Airport |  | TH | 687 |
| 38 | Seattle-Tacoma International Airport |  | US | 673 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 671 |
| 40 | Viracopos International Airport |  | BR | 668 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 617 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 426 | 21m | 244 km | 1,793.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 313 | 24m | 225 km | 1,214.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 303 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 289 | 1h 25m | 910 km | 4,535.1 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 285 | 1h 10m | 770 km | 3,786.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 234 | 19m | 165 km | 665.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 233 | 26m | 275 km | 1,104.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 218 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 175 | 22m | 55 km | 166.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 168 | 26m | 215 km | 622.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 158 | 44m | 241 km | 656.3 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 147 | 1h 44m | 1,423 km | 3,607.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 138 | 1h 39m | 1,156 km | 2,753.0 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-23 13:38 UTC | 2026-06-23 13:53 UTC | 15m |
| OXF3966 | OXF | Falcon Field (KFFZ) | Casa Grande Municipal Airport (KCGZ) | 2026-06-23 12:54 UTC | 2026-06-23 13:47 UTC | 52m |
| FAF4134 | FAF | Istres Le Tube/Istres Air Base (BA 125) Airport (LFMI) | Chalons-Vatry Air Base (LFOK) | 2026-06-23 12:33 UTC | 2026-06-23 13:45 UTC | 1h 12m |
| N1980D |  | Kerrville Municipal/Louis Schreiner Field (KERV) | XS15 (XS15) | 2026-06-23 13:22 UTC | 2026-06-23 13:33 UTC | 11m |
| RNGR850 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | San Jose Island Airport (XS67) | 2026-06-23 13:13 UTC | 2026-06-23 13:33 UTC | 19m |
| SMGLR21 | SMG | Pardubice Airport (LKPD) | Pardubice Airport (LKPD) | 2026-06-23 13:16 UTC | 2026-06-23 13:31 UTC | 14m |
| DOR611 | DOR | Oberpfaffenhofen Airport (EDMO) | Oberpfaffenhofen Airport (EDMO) | 2026-06-23 12:02 UTC | 2026-06-23 13:29 UTC | 1h 26m |
| N19679 |  | Miami-Opa Locka Executive Airport (KOPF) | Miami-Opa Locka Executive Airport (KOPF) | 2026-06-23 12:45 UTC | 2026-06-23 13:29 UTC | 43m |
| ROKT22 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-06-23 13:11 UTC | 2026-06-23 13:25 UTC | 14m |
| N1088R |  | Mahlon Sweet Field (KEUG) | Portland-Hillsboro Airport (KHIO) | 2026-06-23 13:04 UTC | 2026-06-23 13:25 UTC | 20m |
| HK2078G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-23 12:57 UTC | 2026-06-23 13:24 UTC | 27m |
| ARGUE01 | ARG | Danaher Airport (7TX0) | Munday Municipal Airport (K37F) | 2026-06-23 13:04 UTC | 2026-06-23 13:23 UTC | 19m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-23 13:09 UTC | 2026-06-23 13:23 UTC | 13m |
| N780JH |  | Mckinney Ntl Airport (KTKI) | K Ranch Airport (3TE0) | 2026-06-23 12:39 UTC | 2026-06-23 13:22 UTC | 43m |
| SAS7526 | Scandinavian Airlines | Alicante International Airport (LEAL) | Alicante International Airport (LEAL) | 2026-06-23 13:19 UTC | 2026-06-23 13:19 UTC | 0m |
| N487DC |  | Harvey's Acres Airport (OR28) | Independence State Airport (K7S5) | 2026-06-23 12:44 UTC | 2026-06-23 13:14 UTC | 29m |
| N717FH |  | New Century Aircenter Airport (KIXD) | 26MO (26MO) | 2026-06-23 12:49 UTC | 2026-06-23 13:12 UTC | 23m |
| ROKT24 | ROK | Sky Landings Airport (22MS) | Bird Nest Airport (4MS5) | 2026-06-23 13:10 UTC | 2026-06-23 13:12 UTC | 1m |
| ROKT23 | ROK | MS98 (MS98) | Bird Nest Airport (4MS5) | 2026-06-23 13:08 UTC | 2026-06-23 13:12 UTC | 3m |
| ROKT21 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-06-23 12:55 UTC | 2026-06-23 13:12 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
