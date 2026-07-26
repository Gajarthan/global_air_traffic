# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_15:35:05_UTC-green)

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

**Latest saved flight:** 2026-07-26 15:35:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 15:35:05 UTC

- **152,274** saved flights
- **50,532** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **152,274** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,822,406.7 tonnes** estimated CO2 emissions
- **105,646,764 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6156 |
| 2 | SkyWest Airlines | 5560 |
| 3 | EJA | 3004 |
| 4 | IndiGo | 2720 |
| 5 | American Airlines | 2411 |
| 6 | Southwest Airlines | 2314 |
| 7 | ENY | 1898 |
| 8 | Delta Air Lines | 1782 |
| 9 | Lufthansa | 1486 |
| 10 | LATAM Airlines | 1408 |
| 11 | AZU | 1324 |
| 12 | WIF | 1283 |
| 13 | Vueling | 1273 |
| 14 | LXJ | 1171 |
| 15 | AXM | 1089 |
| 16 | Swiss International | 1069 |
| 17 | easyJet | 995 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 949 |
| 20 | QLK | 941 |
| 21 | EJU | 937 |
| 22 | VIV | 840 |
| 23 | CXK | 813 |
| 24 | AEE | 803 |
| 25 | MXY | 801 |
| 26 | GLO | 793 |
| 27 | Air France | 792 |
| 28 | JetBlue | 790 |
| 29 | Cathay Pacific | 784 |
| 30 | United Airlines | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 131129 |
| 2 | 🇪🇸 ES | 9849 |
| 3 | 🇧🇷 BR | 8640 |
| 4 | 🇦🇺 AU | 8595 |
| 5 | 🇮🇳 IN | 8555 |
| 6 | 🇨🇦 CA | 8115 |
| 7 | 🇮🇹 IT | 7896 |
| 8 | 🇩🇪 DE | 7803 |
| 9 | 🇬🇧 GB | 6995 |
| 10 | 🇯🇵 JP | 6314 |
| 11 | 🇫🇷 FR | 6036 |
| 12 | 🇨🇴 CO | 5189 |
| 13 | 🇲🇽 MX | 4387 |
| 14 | 🇬🇷 GR | 4346 |
| 15 | 🇳🇴 NO | 4028 |
| 16 | 🇨🇭 CH | 4005 |
| 17 | 🇹🇷 TR | 3633 |
| 18 | 🇲🇾 MY | 2837 |
| 19 | 🇵🇱 PL | 2608 |
| 20 | 🇿🇦 ZA | 2481 |
| 21 | 🇳🇿 NZ | 2289 |
| 22 | 🇹🇭 TH | 2220 |
| 23 | 🇰🇷 KR | 2079 |
| 24 | 🇵🇭 PH | 2025 |
| 25 | 🇬🇹 GT | 1978 |
| 26 | 🇲🇦 MA | 1550 |
| 27 | 🇲🇪 ME | 1489 |
| 28 | 🇭🇷 HR | 1403 |
| 29 | 🇳🇱 NL | 1401 |
| 30 | 🇲🇴 MO | 1254 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3134 |
| 2 | Denver International Airport |  | US | 2550 |
| 3 | Tokyo International Airport |  | JP | 2006 |
| 4 | Guaymaral Airport |  | CO | 1910 |
| 5 | Indira Gandhi International Airport |  | IN | 1899 |
| 6 | Harry Reid International Airport |  | US | 1873 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1709 |
| 8 | Zurich Airport |  | CH | 1660 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1588 |
| 10 | La Aurora Airport |  | GT | 1533 |
| 11 | Frankfurt am Main International Airport |  | DE | 1435 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1420 |
| 13 | Chicago O'Hare International Airport |  | US | 1399 |
| 14 | El Dorado International Airport |  | CO | 1372 |
| 15 | Salt Lake City International Airport |  | US | 1366 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1296 |
| 17 | Macau International Airport |  | MO | 1254 |
| 18 | Congonhas Airport |  | BR | 1238 |
| 19 | Madrid Barajas International Airport |  | ES | 1215 |
| 20 | Capua Airport |  | IT | 1210 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1177 |
| 22 | Kuala Lumpur International Airport |  | MY | 1090 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 24 | Charlotte/Douglas International Airport |  | US | 1079 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1070 |
| 26 | Charles de Gaulle International Airport |  | FR | 1044 |
| 27 | Bengaluru International Airport |  | IN | 1023 |
| 28 | Malpensa International Airport |  | IT | 1000 |
| 29 | Ninoy Aquino International Airport |  | PH | 948 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 921 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 910 |
| 32 | Barcelona International Airport |  | ES | 909 |
| 33 | Daniel K Inouye International Airport |  | US | 908 |
| 34 | Tenerife Norte Airport |  | ES | 877 |
| 35 | Seattle-Tacoma International Airport |  | US | 875 |
| 36 | Viracopos International Airport |  | BR | 863 |
| 37 | Calgary International Airport |  | CA | 862 |
| 38 | Scottsdale Airport |  | US | 860 |
| 39 | Amsterdam Airport Schiphol |  | NL | 844 |
| 40 | Oslo Gardermoen Airport |  | NO | 835 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 805 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 552 | 21m | 244 km | 2,324.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 369 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 368 | 24m | 225 km | 1,427.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 356 | 1h 9m | 770 km | 4,729.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 280 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 273 | 27m | 275 km | 1,293.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 207 | 44m | 241 km | 859.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 205 | 1h 47m | 1,423 km | 5,031.0 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 200 | 26m | 215 km | 740.7 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 197 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 185 | 27m | 152 km | 483.5 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 184 | 30m | 49 km | 155.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 180 | 1h 15m | 961 km | 2,983.6 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 178 | 18m | 144 km | 442.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 171 | 1h 1m | 695 km | 2,049.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 168 | 51m | 556 km | 1,610.4 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N87RM |  | Skydive New England Airport (ME64) | Skydive New England Airport (ME64) | 2026-07-26 15:23 UTC | 2026-07-26 15:35 UTC | 11m |
| ERU3 | ERU | Massey Farm Airport (AZ34) | Lake Havasu City Airport (KHII) | 2026-07-26 15:14 UTC | 2026-07-26 15:29 UTC | 14m |
| N248M |  | French Valley Airport (KF70) | San Bernardino International Airport (KSBD) | 2026-07-26 15:06 UTC | 2026-07-26 15:25 UTC | 19m |
| N543TH |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-07-26 14:46 UTC | 2026-07-26 15:23 UTC | 36m |
| N911PF |  | Addison Airport (KADS) | Addison Airport (KADS) | 2026-07-26 14:36 UTC | 2026-07-26 15:22 UTC | 46m |
| N839KT |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Cambridge Municipal Airport (KCBG) | 2026-07-26 15:05 UTC | 2026-07-26 15:19 UTC | 14m |
| N21621 |  | Ogden-Hinckley Airport (KOGD) | Brigham City Regional Airport (KBMC) | 2026-07-26 14:28 UTC | 2026-07-26 15:18 UTC | 50m |
| N704LB |  | Teterboro Airport (KTEB) | Lebanon Municipal Airport (KLEB) | 2026-07-26 14:39 UTC | 2026-07-26 15:18 UTC | 39m |
| N167CS |  | K00V (K00V) | Telluride Regional Airport (KTEX) | 2026-07-26 13:22 UTC | 2026-07-26 15:14 UTC | 1h 51m |
| N87RM |  | Skydive New England Airport (ME64) | Skydive New England Airport (ME64) | 2026-07-26 14:15 UTC | 2026-07-26 15:12 UTC | 56m |
| N267TA |  | Jirik Field (OL23) | Walden-Jackson County Airport (K33V) | 2026-07-26 13:26 UTC | 2026-07-26 15:06 UTC | 1h 39m |
| THY663 | Turkish Airlines | Istanbul Airport (LTFM) | Tunis Carthage International Airport (DTTA) | 2026-07-26 12:40 UTC | 2026-07-26 15:06 UTC | 2h 25m |
| N57810 |  | Kansas City Downtown/Wheeler Field (KMKC) | Telluride Regional Airport (KTEX) | 2026-07-26 13:35 UTC | 2026-07-26 15:05 UTC | 1h 30m |
| AAL1090 | American Airlines | Denver International Airport (KDEN) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-26 13:35 UTC | 2026-07-26 15:04 UTC | 1h 29m |
| N2834R |  | Gansner Field (K2O1) | Weed Airport (KO46) | 2026-07-26 14:04 UTC | 2026-07-26 15:02 UTC | 57m |
| N6393C |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-07-26 14:34 UTC | 2026-07-26 14:58 UTC | 24m |
| N307TL |  | Andrews County Airport (KE11) | Telluride Regional Airport (KTEX) | 2026-07-26 13:24 UTC | 2026-07-26 14:56 UTC | 1h 31m |
| 1200 |  | Inyokern Airport (KIYK) | Inyokern Airport (KIYK) | 2026-07-26 14:15 UTC | 2026-07-26 14:55 UTC | 40m |
| 6586H |  | Millard Airport (KMLE) | Lincoln Airport (KLNK) | 2026-07-26 14:05 UTC | 2026-07-26 14:49 UTC | 44m |
| WZZ8XW | Wizz Air | Copernicus Wrocław Airport (EPWR) | Golyama Smolnitsa Airport (LB35) | 2026-07-26 13:18 UTC | 2026-07-26 14:46 UTC | 1h 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
