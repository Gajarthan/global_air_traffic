# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_16:18:08_UTC-green)

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

**Latest saved flight:** 2026-08-04 16:18:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 16:18:08 UTC

- **170,611** saved flights
- **55,574** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **170,611** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,056,417.1 tonnes** estimated CO2 emissions
- **119,212,582 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6794 |
| 2 | SkyWest Airlines | 6227 |
| 3 | EJA | 3384 |
| 4 | IndiGo | 3002 |
| 5 | American Airlines | 2684 |
| 6 | Southwest Airlines | 2684 |
| 7 | ENY | 2125 |
| 8 | Delta Air Lines | 2029 |
| 9 | LATAM Airlines | 1580 |
| 10 | Lufthansa | 1564 |
| 11 | AZU | 1501 |
| 12 | WIF | 1428 |
| 13 | Vueling | 1405 |
| 14 | LXJ | 1336 |
| 15 | AXM | 1176 |
| 16 | Swiss International | 1163 |
| 17 | easyJet | 1146 |
| 18 | EJU | 1045 |
| 19 | Alaska Airlines | 1041 |
| 20 | QLK | 1041 |
| 21 | All Nippon Airways | 1036 |
| 22 | VIV | 941 |
| 23 | Cathay Pacific | 915 |
| 24 | CXK | 908 |
| 25 | United Airlines | 896 |
| 26 | AEE | 892 |
| 27 | GLO | 891 |
| 28 | Air France | 877 |
| 29 | MXY | 869 |
| 30 | JetBlue | 855 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 146971 |
| 2 | 🇪🇸 ES | 10940 |
| 3 | 🇧🇷 BR | 9687 |
| 4 | 🇦🇺 AU | 9521 |
| 5 | 🇮🇳 IN | 9402 |
| 6 | 🇨🇦 CA | 9283 |
| 7 | 🇮🇹 IT | 8827 |
| 8 | 🇩🇪 DE | 8499 |
| 9 | 🇬🇧 GB | 7915 |
| 10 | 🇯🇵 JP | 6871 |
| 11 | 🇫🇷 FR | 6776 |
| 12 | 🇨🇴 CO | 6192 |
| 13 | 🇬🇷 GR | 4968 |
| 14 | 🇲🇽 MX | 4880 |
| 15 | 🇨🇭 CH | 4492 |
| 16 | 🇳🇴 NO | 4456 |
| 17 | 🇹🇷 TR | 4166 |
| 18 | 🇲🇾 MY | 3057 |
| 19 | 🇵🇱 PL | 2869 |
| 20 | 🇿🇦 ZA | 2762 |
| 21 | 🇹🇭 TH | 2486 |
| 22 | 🇳🇿 NZ | 2471 |
| 23 | 🇵🇭 PH | 2255 |
| 24 | 🇬🇹 GT | 2194 |
| 25 | 🇰🇷 KR | 2161 |
| 26 | 🇲🇦 MA | 1721 |
| 27 | 🇭🇷 HR | 1642 |
| 28 | 🇲🇪 ME | 1572 |
| 29 | 🇳🇱 NL | 1553 |
| 30 | 🇲🇴 MO | 1458 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3509 |
| 2 | Denver International Airport |  | US | 2820 |
| 3 | Tokyo International Airport |  | JP | 2156 |
| 4 | Guaymaral Airport |  | CO | 2111 |
| 5 | Indira Gandhi International Airport |  | IN | 2082 |
| 6 | Harry Reid International Airport |  | US | 2049 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1866 |
| 8 | Zurich Airport |  | CH | 1805 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1795 |
| 10 | La Aurora Airport |  | GT | 1692 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1570 |
| 12 | El Dorado International Airport |  | CO | 1547 |
| 13 | Chicago O'Hare International Airport |  | US | 1545 |
| 14 | Salt Lake City International Airport |  | US | 1529 |
| 15 | Frankfurt am Main International Airport |  | DE | 1526 |
| 16 | Macau International Airport |  | MO | 1458 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1401 |
| 18 | Congonhas Airport |  | BR | 1394 |
| 19 | Madrid Barajas International Airport |  | ES | 1338 |
| 20 | Capua Airport |  | IT | 1330 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1290 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1202 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1193 |
| 24 | Charlotte/Douglas International Airport |  | US | 1185 |
| 25 | Charles de Gaulle International Airport |  | FR | 1157 |
| 26 | Kuala Lumpur International Airport |  | MY | 1151 |
| 27 | Malpensa International Airport |  | IT | 1150 |
| 28 | Bengaluru International Airport |  | IN | 1120 |
| 29 | Ninoy Aquino International Airport |  | PH | 1061 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1057 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1053 |
| 32 | Barcelona International Airport |  | ES | 1010 |
| 33 | Daniel K Inouye International Airport |  | US | 989 |
| 34 | Seattle-Tacoma International Airport |  | US | 984 |
| 35 | Viracopos International Airport |  | BR | 970 |
| 36 | Calgary International Airport |  | CA | 965 |
| 37 | Reno/Tahoe International Airport |  | US | 954 |
| 38 | Oslo Gardermoen Airport |  | NO | 950 |
| 39 | Tenerife Norte Airport |  | ES | 948 |
| 40 | Scottsdale Airport |  | US | 939 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 876 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 622 | 21m | 244 km | 2,619.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 405 | 24m | 225 km | 1,571.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 403 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 387 | 1h 8m | 770 km | 5,141.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 318 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 255 | 22m | 55 km | 242.4 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 254 | 44m | 241 km | 1,055.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 234 | 1h 47m | 1,423 km | 5,742.7 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 222 | 26m | 215 km | 822.2 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 215 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 202 | 50m | 556 km | 1,936.3 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 201 | 1h 15m | 961 km | 3,331.7 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 199 | 12m | - | - |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 192 | 1h 38m | 1,156 km | 3,830.3 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 188 | 24m | 218 km | 708.3 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 186 | 1h 1m | 695 km | 2,229.6 t |
| 30 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 185 | 8m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-04 15:03 UTC | 2026-08-04 16:18 UTC | 1h 14m |
| RYR7MP | Ryanair | Bari / Palese International Airport (LIBD) | Malpensa International Airport (LIMC) | 2026-08-04 15:01 UTC | 2026-08-04 16:18 UTC | 1h 16m |
| KSU37 | KSU | 48KS (48KS) | 48KS (48KS) | 2026-08-04 16:02 UTC | 2026-08-04 16:17 UTC | 14m |
| N492ND |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-08-04 14:52 UTC | 2026-08-04 16:15 UTC | 1h 22m |
| N871US |  | Pompano Beach Airpark (KPMP) | Hummingbirds Landing Airport (FL40) | 2026-08-04 15:32 UTC | 2026-08-04 16:12 UTC | 39m |
| N252KM |  | City Of Colorado Springs Municipal Airport (KCOS) | Northern Colorado Regional Airport (KFNL) | 2026-08-04 15:31 UTC | 2026-08-04 16:10 UTC | 39m |
| N5750T |  | St Paul Downtown Holman Field (KSTP) | St Paul Downtown Holman Field (KSTP) | 2026-08-04 14:02 UTC | 2026-08-04 16:05 UTC | 2h 2m |
|  |  | Megara Airport (LGMG) | Megara Airport (LGMG) | 2026-08-04 16:00 UTC | 2026-08-04 16:00 UTC | 0m |
| XAMSL | XAM | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-08-04 14:21 UTC | 2026-08-04 15:59 UTC | 1h 38m |
| CLY285 | CLY | Guernsey Airport (EGJB) | Bournemouth Airport (EGHH) | 2026-08-04 15:27 UTC | 2026-08-04 15:59 UTC | 31m |
| XSN90 | XSN | Lake Tahoe Airport (KTVL) | Palo Alto Airport (KPAO) | 2026-08-04 15:14 UTC | 2026-08-04 15:57 UTC | 42m |
| N2571X |  | Gooden Airpark (KRJD) | Ewing Airport (MD28) | 2026-08-04 15:24 UTC | 2026-08-04 15:56 UTC | 32m |
| N5253X |  | Dupage Airport (KDPA) | 2LL9 (2LL9) | 2026-08-04 15:32 UTC | 2026-08-04 15:54 UTC | 22m |
| N527FB |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-08-04 15:24 UTC | 2026-08-04 15:54 UTC | 29m |
| N18EX |  | Porterville Municipal Airport (KPTV) | Big Bear City Airport (KL35) | 2026-08-04 14:21 UTC | 2026-08-04 15:50 UTC | 1h 29m |
| SAMU13 | SAM | Avignon-Caumont Airport (LFMV) | Marseille Provence Airport (LFML) | 2026-08-04 15:26 UTC | 2026-08-04 15:50 UTC | 24m |
| N1588R |  | Central Jersey Regional Airport (K47N) | Sussex Airport (KFWN) | 2026-08-04 15:31 UTC | 2026-08-04 15:49 UTC | 18m |
| N618JM |  | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | 2026-08-04 15:47 UTC | 2026-08-04 15:47 UTC | 0m |
| N980S |  | Mahlon Sweet Field (KEUG) | Coyote Ridge Airport (17ID) | 2026-08-04 15:09 UTC | 2026-08-04 15:47 UTC | 37m |
| BSM25 | BSM | Rocket Ranch Airport (OK90) | Sandy Creek Ranch Airport (TX47) | 2026-08-04 15:32 UTC | 2026-08-04 15:46 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
