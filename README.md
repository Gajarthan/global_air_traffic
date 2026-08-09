# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_14:32:37_UTC-green)

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

**Latest saved flight:** 2026-08-09 14:32:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 14:32:37 UTC

- **181,201** saved flights
- **57,895** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **181,201** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,178,202.9 tonnes** estimated CO2 emissions
- **126,272,632 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7188 |
| 2 | SkyWest Airlines | 6583 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3180 |
| 5 | Southwest Airlines | 2841 |
| 6 | American Airlines | 2818 |
| 7 | ENY | 2251 |
| 8 | Delta Air Lines | 2143 |
| 9 | LATAM Airlines | 1693 |
| 10 | AZU | 1624 |
| 11 | Lufthansa | 1613 |
| 12 | Vueling | 1502 |
| 13 | WIF | 1501 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1241 |
| 16 | Swiss International | 1237 |
| 17 | AXM | 1226 |
| 18 | QLK | 1116 |
| 19 | EJU | 1109 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 997 |
| 23 | GLO | 967 |
| 24 | AEE | 947 |
| 25 | Cathay Pacific | 947 |
| 26 | CXK | 947 |
| 27 | Air France | 938 |
| 28 | United Airlines | 930 |
| 29 | PGT | 911 |
| 30 | MXY | 908 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154861 |
| 2 | 🇪🇸 ES | 11679 |
| 3 | 🇧🇷 BR | 10402 |
| 4 | 🇦🇺 AU | 10202 |
| 5 | 🇮🇳 IN | 9972 |
| 6 | 🇨🇦 CA | 9860 |
| 7 | 🇮🇹 IT | 9379 |
| 8 | 🇩🇪 DE | 8988 |
| 9 | 🇬🇧 GB | 8386 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7222 |
| 12 | 🇨🇴 CO | 6724 |
| 13 | 🇬🇷 GR | 5310 |
| 14 | 🇲🇽 MX | 5166 |
| 15 | 🇨🇭 CH | 4841 |
| 16 | 🇹🇷 TR | 4676 |
| 17 | 🇳🇴 NO | 4669 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3046 |
| 20 | 🇿🇦 ZA | 2994 |
| 21 | 🇹🇭 TH | 2798 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2299 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1827 |
| 27 | 🇭🇷 HR | 1806 |
| 28 | 🇲🇪 ME | 1644 |
| 29 | 🇳🇱 NL | 1630 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3735 |
| 2 | Denver International Airport |  | US | 2988 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2228 |
| 5 | Guaymaral Airport |  | CO | 2224 |
| 6 | Harry Reid International Airport |  | US | 2127 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1951 |
| 8 | Zurich Airport |  | CH | 1931 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1766 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1616 |
| 14 | El Dorado International Airport |  | CO | 1616 |
| 15 | Frankfurt am Main International Airport |  | DE | 1574 |
| 16 | Macau International Airport |  | MO | 1518 |
| 17 | Congonhas Airport |  | BR | 1507 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1437 |
| 19 | Madrid Barajas International Airport |  | ES | 1427 |
| 20 | Capua Airport |  | IT | 1418 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1352 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1294 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1250 |
| 25 | Charles de Gaulle International Airport |  | FR | 1233 |
| 26 | Charlotte/Douglas International Airport |  | US | 1224 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1182 |
| 29 | Ninoy Aquino International Airport |  | PH | 1135 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1123 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1045 |
| 34 | Daniel K Inouye International Airport |  | US | 1041 |
| 35 | Seattle-Tacoma International Airport |  | US | 1041 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1003 |
| 39 | Tenerife Norte Airport |  | ES | 992 |
| 40 | Vitoria/Foronda Airport |  | ES | 983 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 418 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 305 | 27m | 275 km | 1,445.3 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 255 | 1h 48m | 1,423 km | 6,258.1 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 242 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 240 | 20m | 250 km | 1,036.7 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 228 | 26m | 215 km | 844.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 222 | 19m | 99 km | 380.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 217 | 19m | 144 km | 539.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 214 | 1h 38m | 1,156 km | 4,269.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 210 | 24m | 218 km | 791.2 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N999VP |  | Vogen Airport (IS41) | IS95 (IS95) | 2026-08-09 13:40 UTC | 2026-08-09 14:32 UTC | 52m |
| N469TS |  | Hen & Bacon Airport (90VA) | Orange County Airport (KOMH) | 2026-08-09 14:12 UTC | 2026-08-09 14:27 UTC | 15m |
| RYR4LW | Ryanair | Sofia Airport (LBSF) | Chania International Airport (LGSA) | 2026-08-09 13:17 UTC | 2026-08-09 14:26 UTC | 1h 9m |
| CAP2745 | CAP | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-09 13:56 UTC | 2026-08-09 14:17 UTC | 21m |
| N64053 |  | Martha's Vineyard Airport (KMVY) | Cape Cod Coast Guard Air Station (KFMH) | 2026-08-09 14:04 UTC | 2026-08-09 14:17 UTC | 12m |
| N6201F |  | Gilmer County Airport (K49A) | Blue Ridge Skyport Airport (57GA) | 2026-08-09 14:13 UTC | 2026-08-09 14:17 UTC | 3m |
| N8747H |  | Jirik Field (OL23) | 19OK (19OK) | 2026-08-09 13:38 UTC | 2026-08-09 14:15 UTC | 36m |
| N9529G |  | Middletown Regional/Hook Field (KMWO) | Middletown Regional/Hook Field (KMWO) | 2026-08-09 13:57 UTC | 2026-08-09 14:15 UTC | 17m |
| PROFH | PRO | SBMM (SBMM) | SBMM (SBMM) | 2026-08-09 13:58 UTC | 2026-08-09 14:15 UTC | 16m |
| N241MP |  | Olive Branch/Taylor Field (KOLV) | Tuscaloosa Ntl Airport (KTCL) | 2026-08-09 12:54 UTC | 2026-08-09 14:13 UTC | 1h 18m |
| N6513D |  | Scottsdale Airport (KSDL) | 42AZ (42AZ) | 2026-08-09 13:36 UTC | 2026-08-09 14:12 UTC | 35m |
| HBXTP | HBX | Zweisimmen Airport (LSTZ) | Zurich Airport (LSZH) | 2026-08-09 13:35 UTC | 2026-08-09 14:09 UTC | 34m |
| N412FA |  | Fullerton Municipal Airport (KFUL) | Mc Conville Airstrip (CA42) | 2026-08-09 13:26 UTC | 2026-08-09 14:08 UTC | 41m |
| HBKKI | HBK | Winzeln-Schramberg Airport (EDTW) | Donaueschingen-Villingen Airport (EDTD) | 2026-08-09 13:52 UTC | 2026-08-09 14:07 UTC | 14m |
| AFL273 | AFL | Suvarnabhumi Airport (VTBS) | Bezymyanka Airfield (UWWG) | 2026-08-09 06:54 UTC | 2026-08-09 14:00 UTC | 7h 6m |
| EPI436 | EPI | North Texas Regional/Perrin Field (KGYI) | Jones Field (KF00) | 2026-08-09 12:59 UTC | 2026-08-09 14:00 UTC | 1h 1m |
| EFD3T | EFD | Westerland Sylt Airport (EDXW) | Giebelstadt Airport (EDQG) | 2026-08-09 12:58 UTC | 2026-08-09 13:58 UTC | 1h 0m |
| ASI818 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-09 13:44 UTC | 2026-08-09 13:55 UTC | 11m |
| CHX50 | CHX | Hamburg-Finkenwerder Airport (EDHI) | Hamburg Airport (EDDH) | 2026-08-09 13:37 UTC | 2026-08-09 13:53 UTC | 16m |
| N425KC |  | Middleton Municipal/Morey Field (KC29) | Miller-Herrold Airport (28MI) | 2026-08-09 13:03 UTC | 2026-08-09 13:51 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
