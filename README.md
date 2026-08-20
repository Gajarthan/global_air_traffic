# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_04:44:46_UTC-green)

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

**Latest saved flight:** 2026-08-20 04:44:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 04:44:46 UTC

- **218,195** saved flights
- **68,709** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,195** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,625,564.3 tonnes** estimated CO2 emissions
- **152,206,625 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8714 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3700 |
| 5 | American Airlines | 3636 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2821 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2068 |
| 10 | AZU | 2000 |
| 11 | Vueling | 1827 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1739 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1424 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1362 |
| 20 | EJU | 1355 |
| 21 | Alaska Airlines | 1337 |
| 22 | All Nippon Airways | 1313 |
| 23 | VIV | 1195 |
| 24 | GLO | 1187 |
| 25 | PGT | 1180 |
| 26 | Air France | 1178 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1111 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1090 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184127 |
| 2 | 🇪🇸 ES | 13944 |
| 3 | 🇧🇷 BR | 12592 |
| 4 | 🇦🇺 AU | 12304 |
| 5 | 🇨🇦 CA | 12051 |
| 6 | 🇮🇹 IT | 11563 |
| 7 | 🇮🇳 IN | 11522 |
| 8 | 🇩🇪 DE | 10769 |
| 9 | 🇬🇧 GB | 10217 |
| 10 | 🇨🇴 CO | 8977 |
| 11 | 🇯🇵 JP | 8906 |
| 12 | 🇫🇷 FR | 8668 |
| 13 | 🇬🇷 GR | 6349 |
| 14 | 🇹🇷 TR | 6269 |
| 15 | 🇲🇽 MX | 6094 |
| 16 | 🇨🇭 CH | 5770 |
| 17 | 🇳🇴 NO | 5406 |
| 18 | 🇲🇾 MY | 3761 |
| 19 | 🇿🇦 ZA | 3685 |
| 20 | 🇵🇱 PL | 3598 |
| 21 | 🇹🇭 TH | 3565 |
| 22 | 🇳🇿 NZ | 3035 |
| 23 | 🇵🇭 PH | 2921 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2621 |
| 26 | 🇭🇷 HR | 2390 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1909 |
| 30 | 🇮🇩 ID | 1839 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3575 |
| 3 | Tokyo International Airport |  | JP | 2675 |
| 4 | Indira Gandhi International Airport |  | IN | 2641 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2244 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2213 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2052 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1779 |
| 17 | Madrid Barajas International Airport |  | ES | 1703 |
| 18 | Capua Airport |  | IT | 1655 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1615 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1603 |
| 22 | Macau International Airport |  | MO | 1565 |
| 23 | Malpensa International Airport |  | IT | 1535 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1527 |
| 25 | Charles de Gaulle International Airport |  | FR | 1494 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1387 |
| 28 | Kuala Lumpur International Airport |  | MY | 1384 |
| 29 | Barcelona International Airport |  | ES | 1333 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1331 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1305 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1277 |
| 35 | Calgary International Airport |  | CA | 1234 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Don Mueang International Airport |  | TH | 1176 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1173 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 783 | 21m | 244 km | 3,297.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 539 | 1h 7m | 770 km | 7,160.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 512 | 24m | 225 km | 1,986.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 320 | 1h 49m | 1,423 km | 7,853.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 311 | 1h 7m | 706 km | 3,786.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 272 | 1h 38m | 1,156 km | 5,426.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 259 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 257 | 31m | 369 km | 1,635.9 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 236 | 44m | 555 km | 2,259.8 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAE9834 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-08-19 21:20 UTC | 2026-08-20 04:44 UTC | 7h 24m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-19 17:43 UTC | 2026-08-20 04:41 UTC | 10h 58m |
| ZHJ | ZHJ | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-20 04:08 UTC | 2026-08-20 04:36 UTC | 27m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-20 04:12 UTC | 2026-08-20 04:29 UTC | 16m |
| FIN4J | Finnair | Helsinki Vantaa Airport (EFHK) | Pyhoselka Airport (EFPH) | 2026-08-20 03:38 UTC | 2026-08-20 04:25 UTC | 46m |
| MSR938 | EgyptAir | Al Khawr Airport (OTBK) | Hulwan (HE15) | 2026-08-20 02:01 UTC | 2026-08-20 04:23 UTC | 2h 21m |
| QLK861D | QLK | Brisbane International Airport (YBBN) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-08-20 02:30 UTC | 2026-08-20 04:19 UTC | 1h 49m |
| N114UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-20 03:11 UTC | 2026-08-20 04:12 UTC | 1h 0m |
| N101WL |  | KU42 (KU42) | Nephi Municipal Airport (KU14) | 2026-08-20 03:39 UTC | 2026-08-20 04:07 UTC | 28m |
| EFC69G | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-20 03:51 UTC | 2026-08-20 04:06 UTC | 14m |
| 5YSLQ |  | Nairobi Wilson Airport (HKNW) | Narok Airport (HKNO) | 2026-08-20 03:39 UTC | 2026-08-20 04:05 UTC | 26m |
| SIL1403 | SIL | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-08-20 03:35 UTC | 2026-08-20 04:04 UTC | 29m |
| ANA8441 | All Nippon Airways | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-20 01:08 UTC | 2026-08-20 04:02 UTC | 2h 53m |
| N671PC |  | Las Cruces International Airport (KLRU) | Casas Adobes Airpark (NM69) | 2026-08-20 03:39 UTC | 2026-08-20 03:58 UTC | 19m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-08-20 03:35 UTC | 2026-08-20 03:57 UTC | 22m |
| SFJ77 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-20 02:51 UTC | 2026-08-20 03:56 UTC | 1h 4m |
| AEE572 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Kasteli Airport (LGTL) | 2026-08-20 03:08 UTC | 2026-08-20 03:55 UTC | 47m |
| JMA8660 | JMA | Jomo Kenyatta International Airport (HKJK) | Nakuru Airport (HKNK) | 2026-08-20 03:36 UTC | 2026-08-20 03:55 UTC | 19m |
| SHR11 | SHR | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-08-20 03:54 UTC | 2026-08-20 03:55 UTC | 0m |
| SHR09 | SHR | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-08-20 03:53 UTC | 2026-08-20 03:54 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
