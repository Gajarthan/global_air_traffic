# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_14:12:15_UTC-green)

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

**Latest saved flight:** 2026-08-07 14:12:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 14:12:15 UTC

- **175,377** saved flights
- **56,624** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **175,377** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,110,640.7 tonnes** estimated CO2 emissions
- **122,355,981 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6959 |
| 2 | SkyWest Airlines | 6391 |
| 3 | EJA | 3461 |
| 4 | IndiGo | 3083 |
| 5 | Southwest Airlines | 2756 |
| 6 | American Airlines | 2737 |
| 7 | ENY | 2174 |
| 8 | Delta Air Lines | 2071 |
| 9 | LATAM Airlines | 1622 |
| 10 | Lufthansa | 1582 |
| 11 | AZU | 1554 |
| 12 | WIF | 1470 |
| 13 | Vueling | 1446 |
| 14 | LXJ | 1371 |
| 15 | AXM | 1196 |
| 16 | Swiss International | 1195 |
| 17 | easyJet | 1192 |
| 18 | QLK | 1082 |
| 19 | EJU | 1073 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1065 |
| 22 | VIV | 964 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 931 |
| 25 | GLO | 921 |
| 26 | AEE | 916 |
| 27 | United Airlines | 907 |
| 28 | Air France | 903 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150573 |
| 2 | 🇪🇸 ES | 11238 |
| 3 | 🇧🇷 BR | 9982 |
| 4 | 🇦🇺 AU | 9948 |
| 5 | 🇮🇳 IN | 9663 |
| 6 | 🇨🇦 CA | 9582 |
| 7 | 🇮🇹 IT | 9058 |
| 8 | 🇩🇪 DE | 8703 |
| 9 | 🇬🇧 GB | 8132 |
| 10 | 🇯🇵 JP | 7076 |
| 11 | 🇫🇷 FR | 6975 |
| 12 | 🇨🇴 CO | 6435 |
| 13 | 🇬🇷 GR | 5108 |
| 14 | 🇲🇽 MX | 5009 |
| 15 | 🇨🇭 CH | 4651 |
| 16 | 🇳🇴 NO | 4574 |
| 17 | 🇹🇷 TR | 4330 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2928 |
| 20 | 🇿🇦 ZA | 2860 |
| 21 | 🇹🇭 TH | 2615 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2324 |
| 24 | 🇬🇹 GT | 2231 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1772 |
| 27 | 🇭🇷 HR | 1714 |
| 28 | 🇲🇪 ME | 1604 |
| 29 | 🇳🇱 NL | 1583 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3609 |
| 2 | Denver International Airport |  | US | 2892 |
| 3 | Tokyo International Airport |  | JP | 2208 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2146 |
| 6 | Harry Reid International Airport |  | US | 2092 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1905 |
| 8 | Zurich Airport |  | CH | 1858 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1831 |
| 10 | La Aurora Airport |  | GT | 1718 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1544 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1443 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1422 |
| 19 | Capua Airport |  | IT | 1370 |
| 20 | Madrid Barajas International Airport |  | ES | 1367 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1235 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1194 |
| 26 | Charles de Gaulle International Airport |  | FR | 1192 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1147 |
| 29 | Ninoy Aquino International Airport |  | PH | 1093 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1084 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1082 |
| 32 | Barcelona International Airport |  | ES | 1039 |
| 33 | Daniel K Inouye International Airport |  | US | 1009 |
| 34 | Seattle-Tacoma International Airport |  | US | 1008 |
| 35 | Viracopos International Airport |  | BR | 996 |
| 36 | Calgary International Airport |  | CA | 993 |
| 37 | Reno/Tahoe International Airport |  | US | 992 |
| 38 | Oslo Gardermoen Airport |  | NO | 978 |
| 39 | Tenerife Norte Airport |  | ES | 968 |
| 40 | Amsterdam Airport Schiphol |  | NL | 950 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 640 | 21m | 244 km | 2,694.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 409 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 323 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 265 | 22m | 55 km | 251.9 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 265 | 44m | 241 km | 1,100.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 241 | 1h 48m | 1,423 km | 5,914.5 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 230 | 20m | 250 km | 993.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 224 | 26m | 215 km | 829.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 215 | 20m | 99 km | 368.3 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 210 | 51m | 556 km | 2,013.0 t |
| 22 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 209 | 8m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 209 | 19m | 144 km | 519.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 208 | 1h 15m | 961 km | 3,447.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 199 | 24m | 218 km | 749.7 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 191 | 43m | 452 km | 1,488.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N74882 |  | Boerne Stage Airfield (K5C1) | New Braunfels Ntl Airport (KBAZ) | 2026-08-07 13:51 UTC | 2026-08-07 14:12 UTC | 20m |
| N209K |  | Nashville International Airport (KBNA) | Cedar Crest Field (1TN0) | 2026-08-07 12:35 UTC | 2026-08-07 14:10 UTC | 1h 35m |
| DKFPA | DKF | Puimoisson Airport (LFTP) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-08-07 11:28 UTC | 2026-08-07 14:08 UTC | 2h 40m |
| N78NA |  | Albuquerque International Sunport Airport (KABQ) | Ohkay Owingeh Airport (KE14) | 2026-08-07 13:38 UTC | 2026-08-07 14:03 UTC | 25m |
| HB1630 |  | Amlikon Glider Airport (LSPA) | Amlikon Glider Airport (LSPA) | 2026-08-07 11:32 UTC | 2026-08-07 13:54 UTC | 2h 22m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Lehigh Valley International Airport (KABE) | 2026-08-07 13:01 UTC | 2026-08-07 13:54 UTC | 52m |
| VAJ73G | VAJ | Cologne Bonn Airport (EDDK) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-07 12:19 UTC | 2026-08-07 13:54 UTC | 1h 34m |
| DKEOR | DKE | Dachau-Grobenried Airport (EDMD) | Dachau-Grobenried Airport (EDMD) | 2026-08-07 13:36 UTC | 2026-08-07 13:52 UTC | 15m |
| N622DM |  | Bemaroy Airport (8XS0) | Lone Star Flying Service Airport (XA41) | 2026-08-07 13:46 UTC | 2026-08-07 13:52 UTC | 5m |
| N4851P |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-07 13:33 UTC | 2026-08-07 13:50 UTC | 16m |
| N634DC |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-07 13:32 UTC | 2026-08-07 13:49 UTC | 16m |
| CFCPT | CFC | Vulcan Airport (CFX6) | Cowley Airport (CYYM) | 2026-08-07 13:25 UTC | 2026-08-07 13:46 UTC | 21m |
| BLADE12 | BLA | 4XA5 (4XA5) | Frederick Regional Airport (KFDR) | 2026-08-07 13:13 UTC | 2026-08-07 13:43 UTC | 29m |
| N724JT |  | Westchester County Airport (KHPN) | Waterbury-Oxford Airport (KOXC) | 2026-08-07 13:22 UTC | 2026-08-07 13:38 UTC | 16m |
| N384AJ |  | West Virginia International Yeager Airport (KCRW) | Greenbrier Valley Airport (KLWB) | 2026-08-07 13:25 UTC | 2026-08-07 13:37 UTC | 12m |
| AAL1169 | American Airlines | Toronto Pearson International Airport (CYYZ) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-07 10:57 UTC | 2026-08-07 13:35 UTC | 2h 38m |
| GT409 |  | Saskatoon John G. Diefenbaker International Airport (CYXE) | Lumsden (Colhoun) Airport (CKH8) | 2026-08-07 13:07 UTC | 2026-08-07 13:35 UTC | 27m |
| N635KC |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-08-07 12:50 UTC | 2026-08-07 13:34 UTC | 44m |
| N20015 |  | Mckinney Ntl Airport (KTKI) | Grove Hill Airport (5TX2) | 2026-08-07 12:47 UTC | 2026-08-07 13:33 UTC | 46m |
| N70075 |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-07 13:10 UTC | 2026-08-07 13:33 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
