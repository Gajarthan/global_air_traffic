# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_13:12:42_UTC-green)

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

**Latest saved flight:** 2026-08-17 13:12:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 13:12:42 UTC

- **207,943** saved flights
- **66,090** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,943** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,501,101.1 tonnes** estimated CO2 emissions
- **144,991,367 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8214 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4041 |
| 4 | IndiGo | 3562 |
| 5 | American Airlines | 3456 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2668 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1957 |
| 10 | AZU | 1878 |
| 11 | Lufthansa | 1759 |
| 12 | Vueling | 1729 |
| 13 | WIF | 1673 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1435 |
| 16 | Swiss International | 1385 |
| 17 | AXM | 1362 |
| 18 | United Airlines | 1307 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1268 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1144 |
| 24 | GLO | 1122 |
| 25 | Air France | 1116 |
| 26 | PGT | 1115 |
| 27 | JetBlue | 1064 |
| 28 | AEE | 1063 |
| 29 | WMT | 1053 |
| 30 | Wizz Air | 1027 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176140 |
| 2 | 🇪🇸 ES | 13296 |
| 3 | 🇧🇷 BR | 11903 |
| 4 | 🇦🇺 AU | 11745 |
| 5 | 🇨🇦 CA | 11469 |
| 6 | 🇮🇳 IN | 11110 |
| 7 | 🇮🇹 IT | 10874 |
| 8 | 🇩🇪 DE | 10288 |
| 9 | 🇬🇧 GB | 9689 |
| 10 | 🇯🇵 JP | 8643 |
| 11 | 🇨🇴 CO | 8254 |
| 12 | 🇫🇷 FR | 8237 |
| 13 | 🇬🇷 GR | 6128 |
| 14 | 🇹🇷 TR | 5914 |
| 15 | 🇲🇽 MX | 5842 |
| 16 | 🇨🇭 CH | 5547 |
| 17 | 🇳🇴 NO | 5182 |
| 18 | 🇲🇾 MY | 3590 |
| 19 | 🇿🇦 ZA | 3496 |
| 20 | 🇵🇱 PL | 3426 |
| 21 | 🇹🇭 TH | 3340 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2771 |
| 24 | 🇬🇹 GT | 2655 |
| 25 | 🇰🇷 KR | 2544 |
| 26 | 🇭🇷 HR | 2232 |
| 27 | 🇲🇦 MA | 2100 |
| 28 | 🇳🇱 NL | 1850 |
| 29 | 🇲🇪 ME | 1763 |
| 30 | 🇮🇩 ID | 1723 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4366 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2527 |
| 5 | Guaymaral Airport |  | CO | 2501 |
| 6 | Harry Reid International Airport |  | US | 2346 |
| 7 | Zurich Airport |  | CH | 2169 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2168 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2151 |
| 10 | La Aurora Airport |  | GT | 2021 |
| 11 | Chicago O'Hare International Airport |  | US | 1922 |
| 12 | El Dorado International Airport |  | CO | 1894 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1857 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1733 |
| 16 | Frankfurt am Main International Airport |  | DE | 1715 |
| 17 | Madrid Barajas International Airport |  | ES | 1634 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1580 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1576 |
| 20 | Capua Airport |  | IT | 1574 |
| 21 | Macau International Airport |  | MO | 1545 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1508 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1467 |
| 24 | Malpensa International Airport |  | IT | 1443 |
| 25 | Charles de Gaulle International Airport |  | FR | 1429 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1326 |
| 28 | Ninoy Aquino International Airport |  | PH | 1313 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1284 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Barcelona International Airport |  | ES | 1245 |
| 33 | Seattle-Tacoma International Airport |  | US | 1238 |
| 34 | Viracopos International Airport |  | BR | 1204 |
| 35 | Calgary International Airport |  | CA | 1175 |
| 36 | Oslo Gardermoen Airport |  | NO | 1150 |
| 37 | Vitoria/Foronda Airport |  | ES | 1147 |
| 38 | Reno/Tahoe International Airport |  | US | 1143 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1114 |
| 40 | Daniel K Inouye International Airport |  | US | 1110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1028 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 348 | 27m | 275 km | 1,649.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 344 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 305 | 44m | 241 km | 1,266.9 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 304 | 1h 49m | 1,423 km | 7,460.6 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 264 | 24m | 218 km | 994.6 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 253 | 27m | 215 km | 937.0 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 248 | 1h 37m | 1,156 km | 4,947.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 238 | 19m | 144 km | 592.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 226 | 28m | 152 km | 590.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPSMH | SPS | Poznań-Kobylnica Airport (EPPK) | Poznań-Kobylnica Airport (EPPK) | 2026-08-17 13:02 UTC | 2026-08-17 13:12 UTC | 10m |
| N999VP |  | Vogen Airport (IS41) | Vogen Airport (IS41) | 2026-08-17 12:32 UTC | 2026-08-17 13:02 UTC | 29m |
| N347NA |  | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Tweed/New Haven Airport (KHVN) | 2026-08-17 12:08 UTC | 2026-08-17 13:02 UTC | 53m |
| BULLY28 | BUL | Bertani Ranch Airport (23TS) | Lewis Private Airport (4TE2) | 2026-08-17 12:56 UTC | 2026-08-17 12:57 UTC | 0m |
| N6967C |  | Middle Georgia Regional Airport (KMCN) | Middle Georgia Regional Airport (KMCN) | 2026-08-17 12:39 UTC | 2026-08-17 12:56 UTC | 17m |
| IPTVR | IPT | LICL (LICL) | LICL (LICL) | 2026-08-17 12:31 UTC | 2026-08-17 12:53 UTC | 22m |
| BPO320 | BPO | Bonn-Hangelar Airport (EDKB) | Norvenich Airport (ETNN) | 2026-08-17 11:51 UTC | 2026-08-17 12:51 UTC | 1h 0m |
| N804CT |  | 1MS0 (1MS0) | West Bolivar Flying Service Airport (MS37) | 2026-08-17 12:30 UTC | 2026-08-17 12:41 UTC | 11m |
| N23556 |  | Auburn University Regional Airport (KAUO) | Thomas C Russell Field (KALX) | 2026-08-17 12:10 UTC | 2026-08-17 12:40 UTC | 30m |
| EFC58E | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-17 12:25 UTC | 2026-08-17 12:36 UTC | 10m |
| FFAB123 | FFA | Atsugi Naval Air Facility (RJTA) | Kisarazu Airport (RJTK) | 2026-08-17 12:22 UTC | 2026-08-17 12:35 UTC | 12m |
| N258EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-17 11:01 UTC | 2026-08-17 12:34 UTC | 1h 32m |
| N2095J |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-17 11:57 UTC | 2026-08-17 12:34 UTC | 36m |
| N383AA |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-08-17 12:20 UTC | 2026-08-17 12:32 UTC | 12m |
| VLG4JK | Vueling | Alicante International Airport (LEAL) | Bilbao Airport (LEBB) | 2026-08-17 11:41 UTC | 2026-08-17 12:32 UTC | 51m |
| AKT1700 | AKT | Calgary International Airport (CYYC) | Grande Airport (CFA5) | 2026-08-17 11:44 UTC | 2026-08-17 12:31 UTC | 46m |
| N984CE |  | Oakland County International Airport (KPTK) | Grayling Army Air Field (KGOV) | 2026-08-17 12:03 UTC | 2026-08-17 12:30 UTC | 26m |
| SUI785 | SUI | Kassel-Calden Airport (EDVK) | Friedrichshafen Airport (EDNY) | 2026-08-17 11:35 UTC | 2026-08-17 12:29 UTC | 53m |
| JANET77 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-17 12:13 UTC | 2026-08-17 12:26 UTC | 12m |
| IGO542M | IndiGo | Juhu Aerodrome (VAJJ) | Coimbatore Air Force Station (VOSX) | 2026-08-17 11:07 UTC | 2026-08-17 12:25 UTC | 1h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
