# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_21:42:46_UTC-green)

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

**Latest saved flight:** 2026-06-25 21:42:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-25 21:42:46 UTC

- **120,298** saved flights
- **41,383** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **120,298** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,454,853.9 tonnes** estimated CO2 emissions
- **84,339,358 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4940 |
| 2 | SkyWest Airlines | 4442 |
| 3 | EJA | 2323 |
| 4 | IndiGo | 2309 |
| 5 | American Airlines | 1866 |
| 6 | Southwest Airlines | 1795 |
| 7 | ENY | 1498 |
| 8 | Delta Air Lines | 1425 |
| 9 | Lufthansa | 1317 |
| 10 | Vueling | 1082 |
| 11 | WIF | 1067 |
| 12 | LATAM Airlines | 1065 |
| 13 | AZU | 1001 |
| 14 | AXM | 978 |
| 15 | LXJ | 915 |
| 16 | Swiss International | 843 |
| 17 | All Nippon Airways | 820 |
| 18 | Alaska Airlines | 794 |
| 19 | easyJet | 775 |
| 20 | QLK | 768 |
| 21 | EJU | 753 |
| 22 | Cathay Pacific | 675 |
| 23 | AEE | 670 |
| 24 | Air France | 659 |
| 25 | VIV | 659 |
| 26 | United Airlines | 658 |
| 27 | CXK | 644 |
| 28 | MXY | 630 |
| 29 | AXB | 597 |
| 30 | JetBlue | 595 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 101998 |
| 2 | 🇪🇸 ES | 8168 |
| 3 | 🇮🇳 IN | 7256 |
| 4 | 🇦🇺 AU | 7070 |
| 5 | 🇧🇷 BR | 6613 |
| 6 | 🇩🇪 DE | 6428 |
| 7 | 🇮🇹 IT | 6404 |
| 8 | 🇨🇦 CA | 6325 |
| 9 | 🇯🇵 JP | 5351 |
| 10 | 🇬🇧 GB | 5290 |
| 11 | 🇫🇷 FR | 4785 |
| 12 | 🇨🇴 CO | 4016 |
| 13 | 🇲🇽 MX | 3508 |
| 14 | 🇬🇷 GR | 3437 |
| 15 | 🇳🇴 NO | 3311 |
| 16 | 🇨🇭 CH | 3087 |
| 17 | 🇲🇾 MY | 2539 |
| 18 | 🇹🇷 TR | 2474 |
| 19 | 🇿🇦 ZA | 2021 |
| 20 | 🇵🇱 PL | 1979 |
| 21 | 🇳🇿 NZ | 1942 |
| 22 | 🇹🇭 TH | 1916 |
| 23 | 🇰🇷 KR | 1904 |
| 24 | 🇵🇭 PH | 1721 |
| 25 | 🇬🇹 GT | 1680 |
| 26 | 🇲🇦 MA | 1299 |
| 27 | 🇲🇪 ME | 1199 |
| 28 | 🇲🇴 MO | 1173 |
| 29 | 🇳🇱 NL | 1150 |
| 30 | 🇭🇷 HR | 1040 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2524 |
| 2 | Denver International Airport |  | US | 2022 |
| 3 | Tokyo International Airport |  | JP | 1771 |
| 4 | Indira Gandhi International Airport |  | IN | 1597 |
| 5 | Guaymaral Airport |  | CO | 1506 |
| 6 | Harry Reid International Airport |  | US | 1494 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1459 |
| 8 | Zurich Airport |  | CH | 1339 |
| 9 | La Aurora Airport |  | GT | 1297 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1278 |
| 11 | Frankfurt am Main International Airport |  | DE | 1271 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1191 |
| 13 | Chicago O'Hare International Airport |  | US | 1174 |
| 14 | Macau International Airport |  | MO | 1173 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1040 |
| 17 | Capua Airport |  | IT | 1035 |
| 18 | Madrid Barajas International Airport |  | ES | 1010 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1001 |
| 20 | Kuala Lumpur International Airport |  | MY | 982 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 933 |
| 22 | Congonhas Airport |  | BR | 926 |
| 23 | Charlotte/Douglas International Airport |  | US | 910 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 890 |
| 25 | Charles de Gaulle International Airport |  | FR | 883 |
| 26 | Bengaluru International Airport |  | IN | 874 |
| 27 | Malpensa International Airport |  | IT | 839 |
| 28 | Ninoy Aquino International Airport |  | PH | 797 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 784 |
| 30 | Daniel K Inouye International Airport |  | US | 775 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 761 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 739 |
| 34 | Calgary International Airport |  | CA | 702 |
| 35 | Vitoria/Foronda Airport |  | ES | 702 |
| 36 | Amsterdam Airport Schiphol |  | NL | 696 |
| 37 | Don Mueang International Airport |  | TH | 694 |
| 38 | Seattle-Tacoma International Airport |  | US | 692 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 686 |
| 40 | Scottsdale Airport |  | US | 685 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 627 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 436 | 21m | 244 km | 1,835.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 315 | 24m | 225 km | 1,222.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 308 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 291 | 1h 25m | 910 km | 4,566.5 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 289 | 1h 10m | 770 km | 3,839.1 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 237 | 26m | 275 km | 1,123.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 223 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 174 | 27m | 215 km | 644.4 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 165 | 44m | 241 km | 685.4 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 161 | 27m | 152 km | 420.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 150 | 1h 44m | 1,423 km | 3,681.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 150 | 18m | 144 km | 373.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 141 | 1h 38m | 1,156 km | 2,812.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 136 | 1h 17m | 961 km | 2,254.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N75733 |  | Montgomery-Gibbs Executive Airport (KMYF) | San Bernardino International Airport (KSBD) | 2026-06-25 20:34 UTC | 2026-06-25 21:42 UTC | 1h 8m |
| N92141 |  | Pittsburgh/Butler Regional Airport (KBTP) | Beaver County Airport (KBVI) | 2026-06-25 21:26 UTC | 2026-06-25 21:39 UTC | 13m |
| N197MC |  | Lewis University Airport (KLOT) | Decatur Airport (KDEC) | 2026-06-25 20:34 UTC | 2026-06-25 21:38 UTC | 1h 4m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-06-25 10:11 UTC | 2026-06-25 21:32 UTC | 11h 20m |
| N330RX |  | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | New Smyrna Beach Airport (8FA4) | 2026-06-25 21:20 UTC | 2026-06-25 21:31 UTC | 11m |
| N484MM |  | Stephenville Clark Regional Airport (KSEP) | 30XS (30XS) | 2026-06-25 20:36 UTC | 2026-06-25 21:27 UTC | 51m |
| N408LM |  | Wolf Lake Airport (4AK6) | Talkeetna Airport (PATK) | 2026-06-25 20:53 UTC | 2026-06-25 21:20 UTC | 26m |
| YETI44 | YET | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-06-25 20:54 UTC | 2026-06-25 21:18 UTC | 24m |
| BEAK11 | BEA | Sandy Creek Airport (73TX) | Benson Airstrip (2XS8) | 2026-06-25 21:06 UTC | 2026-06-25 21:16 UTC | 10m |
| UAV15 | UAV | Hansen Airport (11CL) | Hansen Airport (11CL) | 2026-06-25 21:05 UTC | 2026-06-25 21:16 UTC | 10m |
| N563DJ |  | Flying R Airport (11UT) | Flying R Airport (11UT) | 2026-06-25 21:03 UTC | 2026-06-25 21:15 UTC | 12m |
| N7695N |  | Southern California Logistics Airport (KVCV) | Krey Field (0CL1) | 2026-06-25 21:09 UTC | 2026-06-25 21:15 UTC | 5m |
| N2054S |  | Lewis University Airport (KLOT) | Neiner Airport (19LL) | 2026-06-25 20:39 UTC | 2026-06-25 21:13 UTC | 34m |
| N6507Y |  | Roberts Field (KRDM) | Dry Creek Airpark (OG21) | 2026-06-25 21:06 UTC | 2026-06-25 21:13 UTC | 7m |
| N441BW |  | Dane County Regional/Truax Field (KMSN) | Turner Airport (4WI4) | 2026-06-25 20:38 UTC | 2026-06-25 21:12 UTC | 34m |
| N280HL |  | Concord-Padgett Regional Airport (KJQF) | Orlando Executive Airport (KORL) | 2026-06-25 20:02 UTC | 2026-06-25 21:10 UTC | 1h 7m |
| N12FM |  | Delaware Airpark (K33N) | Delaware Airpark (K33N) | 2026-06-25 20:45 UTC | 2026-06-25 21:07 UTC | 21m |
| N90GS |  | Topton Air Estates Airport (0MS0) | AL02 (AL02) | 2026-06-25 20:53 UTC | 2026-06-25 21:05 UTC | 12m |
| ARRIS79 | ARR | Lake Arrowhead Airport (2CN8) | 91CL (91CL) | 2026-06-25 19:20 UTC | 2026-06-25 21:03 UTC | 1h 43m |
| CXK201 | CXK | Camarillo Airport (KCMA) | Oxnard Airport (KOXR) | 2026-06-25 20:37 UTC | 2026-06-25 21:01 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
