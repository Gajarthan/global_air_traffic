# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_16:53:30_UTC-green)

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

**Latest saved flight:** 2026-08-24 16:53:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 16:53:30 UTC

- **232,534** saved flights
- **71,485** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **232,534** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,802,454.4 tonnes** estimated CO2 emissions
- **162,461,124 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9337 |
| 2 | SkyWest Airlines | 8223 |
| 3 | EJA | 4495 |
| 4 | IndiGo | 3938 |
| 5 | American Airlines | 3790 |
| 6 | Southwest Airlines | 3579 |
| 7 | Delta Air Lines | 2968 |
| 8 | ENY | 2829 |
| 9 | LATAM Airlines | 2237 |
| 10 | AZU | 2161 |
| 11 | Vueling | 1989 |
| 12 | Lufthansa | 1896 |
| 13 | WIF | 1850 |
| 14 | LXJ | 1831 |
| 15 | easyJet | 1629 |
| 16 | Swiss International | 1558 |
| 17 | AXM | 1551 |
| 18 | EJU | 1488 |
| 19 | United Airlines | 1476 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1296 |
| 24 | WMT | 1292 |
| 25 | VIV | 1275 |
| 26 | PGT | 1269 |
| 27 | Air France | 1264 |
| 28 | Wizz Air | 1229 |
| 29 | AEE | 1158 |
| 30 | JetBlue | 1156 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 193512 |
| 2 | 🇪🇸 ES | 14937 |
| 3 | 🇧🇷 BR | 13582 |
| 4 | 🇦🇺 AU | 13162 |
| 5 | 🇨🇦 CA | 12791 |
| 6 | 🇮🇹 IT | 12657 |
| 7 | 🇮🇳 IN | 12271 |
| 8 | 🇩🇪 DE | 11465 |
| 9 | 🇬🇧 GB | 10972 |
| 10 | 🇨🇴 CO | 9695 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9313 |
| 13 | 🇹🇷 TR | 6878 |
| 14 | 🇬🇷 GR | 6845 |
| 15 | 🇲🇽 MX | 6455 |
| 16 | 🇨🇭 CH | 6207 |
| 17 | 🇳🇴 NO | 5757 |
| 18 | 🇲🇾 MY | 4143 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4067 |
| 21 | 🇵🇱 PL | 3873 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3184 |
| 24 | 🇬🇹 GT | 2922 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2677 |
| 27 | 🇲🇦 MA | 2362 |
| 28 | 🇲🇪 ME | 2146 |
| 29 | 🇳🇱 NL | 2084 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4834 |
| 2 | Denver International Airport |  | US | 3772 |
| 3 | Indira Gandhi International Airport |  | IN | 2839 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2669 |
| 6 | Harry Reid International Airport |  | US | 2497 |
| 7 | Zurich Airport |  | CH | 2429 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2373 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2337 |
| 10 | La Aurora Airport |  | GT | 2225 |
| 11 | El Dorado International Airport |  | CO | 2159 |
| 12 | Chicago O'Hare International Airport |  | US | 2100 |
| 13 | Salt Lake City International Airport |  | US | 2044 |
| 14 | Congonhas Airport |  | BR | 1981 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1962 |
| 16 | Frankfurt am Main International Airport |  | DE | 1856 |
| 17 | Madrid Barajas International Airport |  | ES | 1828 |
| 18 | Capua Airport |  | IT | 1827 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1750 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1724 |
| 21 | Malpensa International Airport |  | IT | 1668 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1662 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1615 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1533 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1470 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1412 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1404 |
| 32 | Viracopos International Airport |  | BR | 1383 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1361 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1318 |
| 38 | Oslo Gardermoen Airport |  | NO | 1304 |
| 39 | O. R. Tambo International Airport |  | ZA | 1264 |
| 40 | Vitoria/Foronda Airport |  | ES | 1260 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1083 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 847 | 21m | 244 km | 3,566.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 573 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 520 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 384 | 27m | 275 km | 1,819.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 359 | 1h 50m | 1,423 km | 8,810.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 338 | 44m | 241 km | 1,404.0 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 308 | 24m | 218 km | 1,160.4 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 304 | 1h 38m | 1,156 km | 6,064.7 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 269 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 264 | 19m | 144 km | 656.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 248 | 1h 50m | 1,304 km | 5,579.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK119 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-24 16:29 UTC | 2026-08-24 16:53 UTC | 23m |
| GIZMO31 | GIZ | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-08-24 16:35 UTC | 2026-08-24 16:49 UTC | 14m |
| JEDI23 | JED | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Skywest Airpark (62AL) | 2026-08-24 16:24 UTC | 2026-08-24 16:45 UTC | 21m |
| N5852K |  | Albuquerque International Sunport Airport (KABQ) | G Bar F Ranch Airport (NM84) | 2026-08-24 16:01 UTC | 2026-08-24 16:38 UTC | 37m |
| N904AZ |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-08-24 16:03 UTC | 2026-08-24 16:38 UTC | 34m |
| WING81 | WIN | Pope Army Air Field (KPOB) | Marion County Airport (KMAO) | 2026-08-24 16:08 UTC | 2026-08-24 16:36 UTC | 27m |
| ASI625 | ASI | Georgetown Executive Airport (KGTU) | Easterwood Field (KCLL) | 2026-08-24 15:41 UTC | 2026-08-24 16:30 UTC | 48m |
| DAL855 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-24 14:26 UTC | 2026-08-24 16:29 UTC | 2h 3m |
| N707H |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-08-24 16:02 UTC | 2026-08-24 16:27 UTC | 25m |
| SCU57 | SCU | OK13 (OK13) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-24 16:08 UTC | 2026-08-24 16:27 UTC | 19m |
| N57810 |  | Kansas City Downtown/Wheeler Field (KMKC) | Tweed/New Haven Airport (KHVN) | 2026-08-24 14:02 UTC | 2026-08-24 16:24 UTC | 2h 22m |
| N50PE |  | Harrisburg International Airport (KMDT) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-24 15:37 UTC | 2026-08-24 16:23 UTC | 46m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-24 16:09 UTC | 2026-08-24 16:23 UTC | 13m |
| BSM31 | BSM | Durant Regional/Eaker Field (KDUA) | Durant Regional/Eaker Field (KDUA) | 2026-08-24 16:20 UTC | 2026-08-24 16:22 UTC | 2m |
| ELY5468 | ELY | Tirana International Airport Mother Teresa (LATI) | Ben Gurion International Airport (LLBG) | 2026-08-24 14:13 UTC | 2026-08-24 16:22 UTC | 2h 9m |
| JBU2454 | JetBlue | Ronald Reagan Washington Ntl Airport (KDCA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-24 15:15 UTC | 2026-08-24 16:21 UTC | 1h 6m |
| N43556 |  | Rancho Murieta Airport (KRIU) | Chico Regional Airport (KCIC) | 2026-08-24 15:32 UTC | 2026-08-24 16:21 UTC | 48m |
| TGJAC | TGJ | Rnk Ranch Airport (8TS8) | Maverick County Memorial International Airport (K5T9) | 2026-08-24 15:42 UTC | 2026-08-24 16:19 UTC | 37m |
| N754FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-24 16:04 UTC | 2026-08-24 16:19 UTC | 14m |
| N1004E |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-24 15:35 UTC | 2026-08-24 16:18 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
