# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_12:21:36_UTC-green)

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

**Latest saved flight:** 2026-08-01 12:21:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 12:21:36 UTC

- **164,332** saved flights
- **54,035** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **164,332** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,975,474.0 tonnes** estimated CO2 emissions
- **114,520,232 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6565 |
| 2 | SkyWest Airlines | 5982 |
| 3 | EJA | 3255 |
| 4 | IndiGo | 2895 |
| 5 | American Airlines | 2590 |
| 6 | Southwest Airlines | 2578 |
| 7 | ENY | 2041 |
| 8 | Delta Air Lines | 1959 |
| 9 | LATAM Airlines | 1534 |
| 10 | Lufthansa | 1533 |
| 11 | AZU | 1440 |
| 12 | WIF | 1385 |
| 13 | Vueling | 1358 |
| 14 | LXJ | 1274 |
| 15 | AXM | 1140 |
| 16 | Swiss International | 1128 |
| 17 | easyJet | 1079 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1011 |
| 20 | All Nippon Airways | 1009 |
| 21 | EJU | 1004 |
| 22 | VIV | 907 |
| 23 | CXK | 879 |
| 24 | Cathay Pacific | 874 |
| 25 | United Airlines | 866 |
| 26 | AEE | 862 |
| 27 | GLO | 858 |
| 28 | Air France | 850 |
| 29 | MXY | 846 |
| 30 | JetBlue | 836 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141828 |
| 2 | 🇪🇸 ES | 10519 |
| 3 | 🇧🇷 BR | 9359 |
| 4 | 🇦🇺 AU | 9253 |
| 5 | 🇮🇳 IN | 9089 |
| 6 | 🇨🇦 CA | 8941 |
| 7 | 🇮🇹 IT | 8482 |
| 8 | 🇩🇪 DE | 8230 |
| 9 | 🇬🇧 GB | 7560 |
| 10 | 🇯🇵 JP | 6657 |
| 11 | 🇫🇷 FR | 6507 |
| 12 | 🇨🇴 CO | 5870 |
| 13 | 🇬🇷 GR | 4735 |
| 14 | 🇲🇽 MX | 4705 |
| 15 | 🇳🇴 NO | 4332 |
| 16 | 🇨🇭 CH | 4323 |
| 17 | 🇹🇷 TR | 3931 |
| 18 | 🇲🇾 MY | 2965 |
| 19 | 🇵🇱 PL | 2785 |
| 20 | 🇿🇦 ZA | 2681 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2360 |
| 23 | 🇵🇭 PH | 2172 |
| 24 | 🇰🇷 KR | 2132 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1657 |
| 27 | 🇭🇷 HR | 1549 |
| 28 | 🇲🇪 ME | 1541 |
| 29 | 🇳🇱 NL | 1492 |
| 30 | 🇲🇴 MO | 1391 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3351 |
| 2 | Denver International Airport |  | US | 2730 |
| 3 | Tokyo International Airport |  | JP | 2095 |
| 4 | Guaymaral Airport |  | CO | 2063 |
| 5 | Indira Gandhi International Airport |  | IN | 2014 |
| 6 | Harry Reid International Airport |  | US | 1990 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1812 |
| 8 | Zurich Airport |  | CH | 1749 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1726 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1523 |
| 12 | El Dorado International Airport |  | CO | 1504 |
| 13 | Frankfurt am Main International Airport |  | DE | 1489 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1478 |
| 16 | Macau International Airport |  | MO | 1391 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1378 |
| 18 | Congonhas Airport |  | BR | 1356 |
| 19 | Madrid Barajas International Airport |  | ES | 1297 |
| 20 | Capua Airport |  | IT | 1289 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1252 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1161 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Charles de Gaulle International Airport |  | FR | 1123 |
| 26 | Kuala Lumpur International Airport |  | MY | 1123 |
| 27 | Malpensa International Airport |  | IT | 1088 |
| 28 | Bengaluru International Airport |  | IN | 1079 |
| 29 | Ninoy Aquino International Airport |  | PH | 1021 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1007 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 32 | Barcelona International Airport |  | ES | 971 |
| 33 | Daniel K Inouye International Airport |  | US | 959 |
| 34 | Seattle-Tacoma International Airport |  | US | 952 |
| 35 | Calgary International Airport |  | CA | 937 |
| 36 | Viracopos International Airport |  | BR | 931 |
| 37 | Tenerife Norte Airport |  | ES | 918 |
| 38 | Oslo Gardermoen Airport |  | NO | 917 |
| 39 | Scottsdale Airport |  | US | 917 |
| 40 | Reno/Tahoe International Airport |  | US | 902 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 597 | 21m | 244 km | 2,513.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 377 | 1h 9m | 770 km | 5,008.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 306 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 244 | 22m | 55 km | 231.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 241 | 19m | 165 km | 685.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 225 | 1h 47m | 1,423 km | 5,521.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 214 | 26m | 215 km | 792.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 211 | 20m | 250 km | 911.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 195 | 1h 15m | 961 km | 3,232.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 193 | 18m | 144 km | 480.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 191 | 31m | 369 km | 1,215.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 183 | 1h 39m | 1,156 km | 3,650.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N738SY |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-01 11:51 UTC | 2026-08-01 12:21 UTC | 30m |
| CPI283 | CPI | Ciampino Airport (LIRA) | Alghero / Fertilia Airport (LIEA) | 2026-08-01 11:46 UTC | 2026-08-01 12:21 UTC | 34m |
| STW171 | STW | Cardak Airport (LTAY) | Sheremetyevo International Airport (UUEE) | 2026-08-01 06:36 UTC | 2026-08-01 12:15 UTC | 5h 38m |
| CSN5094 | China Southern | London Gatwick Airport (EGKK) | Pushkin Airport (ULLP) | 2026-08-01 10:13 UTC | 2026-08-01 12:13 UTC | 2h 0m |
| SCU57 | SCU | Pheasant Wings Airport (26OK) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-01 11:56 UTC | 2026-08-01 12:13 UTC | 16m |
| TOM10J | TOM | Ibiza Airport (LEIB) | Exeter International Airport (EGTE) | 2026-08-01 08:31 UTC | 2026-08-01 12:10 UTC | 3h 39m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-07-31 21:56 UTC | 2026-08-01 12:03 UTC | 14h 6m |
| SWE32A | SWE | Lulea Airport (ESPA) | Umea Airport (ESNU) | 2026-08-01 11:25 UTC | 2026-08-01 11:50 UTC | 25m |
| HBPBB | HBP | Birrfeld Airport (LSZF) | Donaueschingen-Villingen Airport (EDTD) | 2026-08-01 10:48 UTC | 2026-08-01 11:49 UTC | 1h 1m |
| EIN3GM | Aer Lingus | Munich International Airport (EDDM) | Dublin Airport (EIDW) | 2026-08-01 09:34 UTC | 2026-08-01 11:42 UTC | 2h 7m |
| AZG9602 | AZG | Oslo Gardermoen Airport (ENGM) | Macau International Airport (VMMC) | 2026-07-31 18:15 UTC | 2026-08-01 11:40 UTC | 17h 24m |
| GBMCV | GBM | Netherthorpe Airfield (EGNF) | Netherthorpe Airfield (EGNF) | 2026-08-01 11:37 UTC | 2026-08-01 11:39 UTC | 1m |
| AXM5309 | AXM | Kota Kinabalu International Airport (WBKK) | Changi Air Base (WSAC) | 2026-08-01 09:57 UTC | 2026-08-01 11:37 UTC | 1h 40m |
| IGO5EC | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Birsa Munda Airport (VERC) | 2026-08-01 10:54 UTC | 2026-08-01 11:35 UTC | 41m |
| AMU861 | AMU | Narita International Airport (RJAA) | Chek Lap Kok International Airport (VHHH) | 2026-08-01 07:40 UTC | 2026-08-01 11:34 UTC | 3h 53m |
| LSA201 | LSA | Ciampino Airport (LIRA) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-01 11:05 UTC | 2026-08-01 11:31 UTC | 26m |
| OEXSR | OEX | Salzburg Airport (LOWS) | Salzburg Airport (LOWS) | 2026-08-01 11:26 UTC | 2026-08-01 11:31 UTC | 4m |
| EJU64LG | EJU | Malpensa International Airport (LIMC) | Bari / Palese International Airport (LIBD) | 2026-08-01 10:13 UTC | 2026-08-01 11:28 UTC | 1h 14m |
| N364EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-01 08:15 UTC | 2026-08-01 11:25 UTC | 3h 9m |
| WMT749 | WMT | Cluj-Napoca International Airport (LRCL) | Malpensa International Airport (LIMC) | 2026-08-01 09:21 UTC | 2026-08-01 11:22 UTC | 2h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
