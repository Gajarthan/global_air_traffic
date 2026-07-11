# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_11:22:12_UTC-green)

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

**Latest saved flight:** 2026-07-11 11:22:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 11:22:12 UTC

- **136,783** saved flights
- **46,159** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **136,783** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,644,247.6 tonnes** estimated CO2 emissions
- **95,318,700 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5553 |
| 2 | SkyWest Airlines | 5014 |
| 3 | EJA | 2679 |
| 4 | IndiGo | 2528 |
| 5 | American Airlines | 2150 |
| 6 | Southwest Airlines | 2060 |
| 7 | ENY | 1715 |
| 8 | Delta Air Lines | 1629 |
| 9 | Lufthansa | 1403 |
| 10 | LATAM Airlines | 1253 |
| 11 | WIF | 1187 |
| 12 | Vueling | 1185 |
| 13 | AZU | 1173 |
| 14 | LXJ | 1051 |
| 15 | AXM | 1032 |
| 16 | Swiss International | 978 |
| 17 | All Nippon Airways | 890 |
| 18 | easyJet | 886 |
| 19 | Alaska Airlines | 864 |
| 20 | QLK | 856 |
| 21 | EJU | 841 |
| 22 | VIV | 747 |
| 23 | AEE | 740 |
| 24 | Air France | 732 |
| 25 | CXK | 730 |
| 26 | Cathay Pacific | 726 |
| 27 | JetBlue | 718 |
| 28 | United Airlines | 718 |
| 29 | MXY | 709 |
| 30 | GLO | 698 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 117374 |
| 2 | 🇪🇸 ES | 9013 |
| 3 | 🇮🇳 IN | 7929 |
| 4 | 🇦🇺 AU | 7873 |
| 5 | 🇧🇷 BR | 7704 |
| 6 | 🇨🇦 CA | 7215 |
| 7 | 🇩🇪 DE | 7144 |
| 8 | 🇮🇹 IT | 7114 |
| 9 | 🇬🇧 GB | 6201 |
| 10 | 🇯🇵 JP | 5816 |
| 11 | 🇫🇷 FR | 5443 |
| 12 | 🇨🇴 CO | 4284 |
| 13 | 🇲🇽 MX | 3964 |
| 14 | 🇬🇷 GR | 3893 |
| 15 | 🇳🇴 NO | 3703 |
| 16 | 🇨🇭 CH | 3558 |
| 17 | 🇹🇷 TR | 3166 |
| 18 | 🇲🇾 MY | 2681 |
| 19 | 🇵🇱 PL | 2275 |
| 20 | 🇿🇦 ZA | 2249 |
| 21 | 🇳🇿 NZ | 2121 |
| 22 | 🇹🇭 TH | 2087 |
| 23 | 🇰🇷 KR | 1996 |
| 24 | 🇵🇭 PH | 1879 |
| 25 | 🇬🇹 GT | 1834 |
| 26 | 🇲🇦 MA | 1436 |
| 27 | 🇲🇪 ME | 1359 |
| 28 | 🇳🇱 NL | 1274 |
| 29 | 🇭🇷 HR | 1232 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2844 |
| 2 | Denver International Airport |  | US | 2290 |
| 3 | Tokyo International Airport |  | JP | 1897 |
| 4 | Indira Gandhi International Airport |  | IN | 1750 |
| 5 | Harry Reid International Airport |  | US | 1713 |
| 6 | Guaymaral Airport |  | CO | 1654 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1592 |
| 8 | Zurich Airport |  | CH | 1526 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1446 |
| 10 | La Aurora Airport |  | GT | 1417 |
| 11 | Frankfurt am Main International Airport |  | DE | 1359 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1312 |
| 13 | Chicago O'Hare International Airport |  | US | 1293 |
| 14 | El Dorado International Airport |  | CO | 1214 |
| 15 | Salt Lake City International Airport |  | US | 1212 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1180 |
| 18 | Madrid Barajas International Airport |  | ES | 1112 |
| 19 | Capua Airport |  | IT | 1109 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1107 |
| 21 | Congonhas Airport |  | BR | 1095 |
| 22 | Kuala Lumpur International Airport |  | MY | 1040 |
| 23 | Charlotte/Douglas International Airport |  | US | 1000 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 976 |
| 26 | Bengaluru International Airport |  | IN | 952 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 940 |
| 28 | Malpensa International Airport |  | IT | 896 |
| 29 | Ninoy Aquino International Airport |  | PH | 874 |
| 30 | Daniel K Inouye International Airport |  | US | 842 |
| 31 | Barcelona International Airport |  | ES | 834 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 832 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 806 |
| 35 | Calgary International Airport |  | CA | 797 |
| 36 | Scottsdale Airport |  | US | 784 |
| 37 | Viracopos International Airport |  | BR | 782 |
| 38 | Seattle-Tacoma International Airport |  | US | 781 |
| 39 | Vitoria/Foronda Airport |  | ES | 770 |
| 40 | Amsterdam Airport Schiphol |  | NL | 764 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 696 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 493 | 21m | 244 km | 2,075.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 339 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 337 | 24m | 225 km | 1,307.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 292 | 14m | 114 km | 572.7 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 255 | 26m | 275 km | 1,208.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 250 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 201 | 22m | 55 km | 191.0 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 184 | 1h 46m | 1,423 km | 4,515.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 181 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 170 | 20m | 250 km | 734.3 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 164 | 18m | 144 km | 407.9 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 164 | 30m | 49 km | 138.6 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-11 11:11 UTC | 2026-07-11 11:22 UTC | 10m |
| GCDMX | GCD | Gloucestershire Airport (EGBJ) | Gloucestershire Airport (EGBJ) | 2026-07-11 11:05 UTC | 2026-07-11 11:21 UTC | 16m |
| N7424X |  | Chandler Municipal Airport (KCHD) | Marana Regional Airport (KAVQ) | 2026-07-11 10:41 UTC | 2026-07-11 11:20 UTC | 39m |
| VOE80DP | VOE | Bologna / Borgo Panigale Airport (LIPE) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-11 10:38 UTC | 2026-07-11 11:19 UTC | 41m |
| DFALB | DFA | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-07-11 07:01 UTC | 2026-07-11 11:19 UTC | 4h 17m |
| N262GF |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Marcellus Airport (NK71) | 2026-07-11 10:29 UTC | 2026-07-11 11:19 UTC | 49m |
| ABY369 | ABY | Nariya Airport (OENR) | Sirri Island Airport (OIBS) | 2026-07-11 10:27 UTC | 2026-07-11 11:15 UTC | 47m |
| DKKSZ | DKK | Schanis Airport (LSZX) | Samedan Airport (LSZS) | 2026-07-11 09:44 UTC | 2026-07-11 11:09 UTC | 1h 24m |
| HBWAT | HBW | Buttwil Airport (LSZU) | Buttwil Airport (LSZU) | 2026-07-11 10:29 UTC | 2026-07-11 11:07 UTC | 37m |
| CXK219 | CXK | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-07-11 10:33 UTC | 2026-07-11 11:06 UTC | 32m |
| MAI336 | MAI | LRPV (LRPV) | LRPV (LRPV) | 2026-07-11 10:52 UTC | 2026-07-11 10:58 UTC | 6m |
| DMFGK | DMF | Pattonville Airport (EDTQ) | Walldurn Airport (EDEW) | 2026-07-11 10:29 UTC | 2026-07-11 10:57 UTC | 28m |
| RYR9CU | Ryanair | Cologne Bonn Airport (EDDK) | Palermo / Punta Raisi Airport (LICJ) | 2026-07-11 09:04 UTC | 2026-07-11 10:53 UTC | 1h 48m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-07-11 07:10 UTC | 2026-07-11 10:52 UTC | 3h 42m |
| LOT577 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Visoko Sport Airfield (LQVI) | 2026-07-11 09:34 UTC | 2026-07-11 10:51 UTC | 1h 17m |
| RYR47GU | Ryanair | Lisbon Portela Airport (LPPT) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-11 07:19 UTC | 2026-07-11 10:50 UTC | 3h 31m |
| RYS7723 | RYS | Copernicus Wrocław Airport (EPWR) | Larnaca International Airport (LCLK) | 2026-07-11 07:42 UTC | 2026-07-11 10:46 UTC | 3h 3m |
| DEZCD | DEZ | Aschaffenburg Airport (EDFC) | Aschaffenburg Airport (EDFC) | 2026-07-11 09:38 UTC | 2026-07-11 10:44 UTC | 1h 6m |
| N769SA |  | Charleston Executive Airport (KJZI) | Charleston Executive Airport (KJZI) | 2026-07-11 10:27 UTC | 2026-07-11 10:43 UTC | 15m |
| IGO7642 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-07-11 10:11 UTC | 2026-07-11 10:39 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
