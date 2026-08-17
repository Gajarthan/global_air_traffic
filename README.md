# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_20:53:47_UTC-green)

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

**Latest saved flight:** 2026-08-17 20:53:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 20:53:47 UTC

- **209,989** saved flights
- **66,855** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **209,989** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,525,013.2 tonnes** estimated CO2 emissions
- **146,377,579 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8314 |
| 2 | SkyWest Airlines | 7549 |
| 3 | EJA | 4099 |
| 4 | IndiGo | 3575 |
| 5 | American Airlines | 3512 |
| 6 | Southwest Airlines | 3376 |
| 7 | Delta Air Lines | 2716 |
| 8 | ENY | 2615 |
| 9 | LATAM Airlines | 1980 |
| 10 | AZU | 1903 |
| 11 | Lufthansa | 1769 |
| 12 | Vueling | 1749 |
| 13 | WIF | 1691 |
| 14 | LXJ | 1661 |
| 15 | easyJet | 1457 |
| 16 | Swiss International | 1403 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1332 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1291 |
| 21 | EJU | 1284 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1156 |
| 24 | GLO | 1137 |
| 25 | Air France | 1133 |
| 26 | PGT | 1123 |
| 27 | JetBlue | 1075 |
| 28 | AEE | 1068 |
| 29 | WMT | 1066 |
| 30 | Wizz Air | 1043 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 177987 |
| 2 | 🇪🇸 ES | 13443 |
| 3 | 🇧🇷 BR | 12053 |
| 4 | 🇦🇺 AU | 11751 |
| 5 | 🇨🇦 CA | 11610 |
| 6 | 🇮🇳 IN | 11156 |
| 7 | 🇮🇹 IT | 10990 |
| 8 | 🇩🇪 DE | 10375 |
| 9 | 🇬🇧 GB | 9802 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8415 |
| 12 | 🇫🇷 FR | 8345 |
| 13 | 🇬🇷 GR | 6177 |
| 14 | 🇹🇷 TR | 5984 |
| 15 | 🇲🇽 MX | 5900 |
| 16 | 🇨🇭 CH | 5583 |
| 17 | 🇳🇴 NO | 5236 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3517 |
| 20 | 🇵🇱 PL | 3472 |
| 21 | 🇹🇭 TH | 3354 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2776 |
| 24 | 🇬🇹 GT | 2696 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2261 |
| 27 | 🇲🇦 MA | 2121 |
| 28 | 🇳🇱 NL | 1872 |
| 29 | 🇲🇪 ME | 1788 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4412 |
| 2 | Denver International Airport |  | US | 3432 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2539 |
| 5 | Guaymaral Airport |  | CO | 2529 |
| 6 | Harry Reid International Airport |  | US | 2360 |
| 7 | Zurich Airport |  | CH | 2189 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2181 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2174 |
| 10 | La Aurora Airport |  | GT | 2050 |
| 11 | Chicago O'Hare International Airport |  | US | 1947 |
| 12 | El Dorado International Airport |  | CO | 1917 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1871 |
| 14 | Salt Lake City International Airport |  | US | 1860 |
| 15 | Congonhas Airport |  | BR | 1754 |
| 16 | Frankfurt am Main International Airport |  | DE | 1722 |
| 17 | Madrid Barajas International Airport |  | ES | 1643 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1592 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1591 |
| 20 | Capua Airport |  | IT | 1584 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1530 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1469 |
| 24 | Malpensa International Airport |  | IT | 1453 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1421 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1315 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1299 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1272 |
| 32 | Barcelona International Airport |  | ES | 1260 |
| 33 | Seattle-Tacoma International Airport |  | US | 1245 |
| 34 | Viracopos International Airport |  | BR | 1220 |
| 35 | Calgary International Airport |  | CA | 1190 |
| 36 | Oslo Gardermoen Airport |  | NO | 1161 |
| 37 | Vitoria/Foronda Airport |  | ES | 1160 |
| 38 | Reno/Tahoe International Airport |  | US | 1148 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1132 |
| 40 | Daniel K Inouye International Airport |  | US | 1114 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 740 | 21m | 244 km | 3,115.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 477 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 425 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 308 | 44m | 241 km | 1,279.4 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 307 | 1h 49m | 1,423 km | 7,534.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 289 | 22m | 55 km | 274.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 250 | 1h 37m | 1,156 km | 4,987.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 249 | 1h 14m | 961 km | 4,127.3 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 248 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 241 | 19m | 144 km | 599.5 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 229 | 28m | 152 km | 598.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 225 | 1h 49m | 1,304 km | 5,061.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1926F |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-08-17 19:59 UTC | 2026-08-17 20:53 UTC | 54m |
| AAL133 | American Airlines | Dublin Airport (EIDW) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-17 11:52 UTC | 2026-08-17 20:50 UTC | 8h 58m |
| N680H |  | Wausau Downtown Airport (KAUW) | Central Wisconsin Airport (KCWA) | 2026-08-17 20:37 UTC | 2026-08-17 20:49 UTC | 12m |
| N414UH |  | UT08 (UT08) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-17 20:31 UTC | 2026-08-17 20:47 UTC | 15m |
| N4603W |  | Rio Vista Municipal Airport (KO88) | Rio Vista Municipal Airport (KO88) | 2026-08-17 20:33 UTC | 2026-08-17 20:44 UTC | 11m |
| N16BT |  | Austin-Bergstrom International Airport (KAUS) | Addison Airport (KADS) | 2026-08-17 19:14 UTC | 2026-08-17 20:44 UTC | 1h 29m |
| N280FG |  | Trenton Mercer Airport (KTTN) | Trenton Mercer Airport (KTTN) | 2026-08-17 19:39 UTC | 2026-08-17 20:44 UTC | 1h 4m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-08-17 19:04 UTC | 2026-08-17 20:38 UTC | 1h 34m |
| N659AC |  | MI44 (MI44) | Ann Arbor Municipal Airport (KARB) | 2026-08-17 20:00 UTC | 2026-08-17 20:34 UTC | 33m |
| LOKI79 | LOK | Fassberg Airport (ETHS) | Fassberg Airport (ETHS) | 2026-08-17 19:08 UTC | 2026-08-17 20:32 UTC | 1h 24m |
| N1934F |  | Gerald R Ford International Airport (KGRR) | Gaylord Regional Airport (KGLR) | 2026-08-17 20:09 UTC | 2026-08-17 20:31 UTC | 21m |
| EJA845 | EJA | Westchester County Airport (KHPN) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-17 19:04 UTC | 2026-08-17 20:30 UTC | 1h 26m |
| N733EB |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-17 20:09 UTC | 2026-08-17 20:29 UTC | 19m |
| N73PG |  | Dallas Executive Airport (KRBD) | Cisco Municipal Airport (K3F2) | 2026-08-17 19:56 UTC | 2026-08-17 20:28 UTC | 31m |
| TWY271 | TWY | San Antonio International Airport (KSAT) | Cavern City Air Trml Airport (KCNM) | 2026-08-17 19:32 UTC | 2026-08-17 20:25 UTC | 53m |
| N936JG |  | Meadows Field (KBFL) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-08-17 20:07 UTC | 2026-08-17 20:25 UTC | 17m |
| N797V |  | Morgan County Airport (K42U) | Evanston-Uinta County Burns Field (KEVW) | 2026-08-17 19:37 UTC | 2026-08-17 20:25 UTC | 48m |
| N3788X |  | Olbia / Costa Smeralda Airport (LIEO) | Grenoble Le Versoud Airport (LFLG) | 2026-08-17 19:24 UTC | 2026-08-17 20:24 UTC | 1h 0m |
| N84G |  | Caldwell Executive Airport (KEUL) | Pocatello Regional Airport (KPIH) | 2026-08-17 18:49 UTC | 2026-08-17 20:24 UTC | 1h 35m |
| JPR09 | JPR | Methow Valley State Airport (KS52) | Green Valley Airfield (WA25) | 2026-08-17 20:15 UTC | 2026-08-17 20:24 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
