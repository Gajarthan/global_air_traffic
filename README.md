# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_08:20:43_UTC-green)

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

**Latest saved flight:** 2026-08-01 08:20:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 08:20:43 UTC

- **164,020** saved flights
- **53,964** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **164,020** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,969,946.8 tonnes** estimated CO2 emissions
- **114,199,813 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6547 |
| 2 | SkyWest Airlines | 5982 |
| 3 | EJA | 3255 |
| 4 | IndiGo | 2881 |
| 5 | American Airlines | 2590 |
| 6 | Southwest Airlines | 2578 |
| 7 | ENY | 2041 |
| 8 | Delta Air Lines | 1958 |
| 9 | LATAM Airlines | 1533 |
| 10 | Lufthansa | 1532 |
| 11 | AZU | 1439 |
| 12 | WIF | 1379 |
| 13 | Vueling | 1357 |
| 14 | LXJ | 1274 |
| 15 | AXM | 1133 |
| 16 | Swiss International | 1127 |
| 17 | easyJet | 1073 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1011 |
| 20 | EJU | 1003 |
| 21 | All Nippon Airways | 1002 |
| 22 | VIV | 906 |
| 23 | CXK | 879 |
| 24 | Cathay Pacific | 871 |
| 25 | United Airlines | 863 |
| 26 | GLO | 858 |
| 27 | AEE | 857 |
| 28 | MXY | 846 |
| 29 | Air France | 844 |
| 30 | JetBlue | 836 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141797 |
| 2 | 🇪🇸 ES | 10483 |
| 3 | 🇧🇷 BR | 9352 |
| 4 | 🇦🇺 AU | 9251 |
| 5 | 🇮🇳 IN | 9046 |
| 6 | 🇨🇦 CA | 8938 |
| 7 | 🇮🇹 IT | 8445 |
| 8 | 🇩🇪 DE | 8215 |
| 9 | 🇬🇧 GB | 7519 |
| 10 | 🇯🇵 JP | 6621 |
| 11 | 🇫🇷 FR | 6474 |
| 12 | 🇨🇴 CO | 5865 |
| 13 | 🇬🇷 GR | 4712 |
| 14 | 🇲🇽 MX | 4703 |
| 15 | 🇳🇴 NO | 4312 |
| 16 | 🇨🇭 CH | 4305 |
| 17 | 🇹🇷 TR | 3918 |
| 18 | 🇲🇾 MY | 2948 |
| 19 | 🇵🇱 PL | 2778 |
| 20 | 🇿🇦 ZA | 2659 |
| 21 | 🇳🇿 NZ | 2408 |
| 22 | 🇹🇭 TH | 2337 |
| 23 | 🇵🇭 PH | 2154 |
| 24 | 🇰🇷 KR | 2126 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1654 |
| 27 | 🇭🇷 HR | 1542 |
| 28 | 🇲🇪 ME | 1538 |
| 29 | 🇳🇱 NL | 1487 |
| 30 | 🇲🇴 MO | 1384 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3351 |
| 2 | Denver International Airport |  | US | 2730 |
| 3 | Tokyo International Airport |  | JP | 2084 |
| 4 | Guaymaral Airport |  | CO | 2063 |
| 5 | Indira Gandhi International Airport |  | IN | 2008 |
| 6 | Harry Reid International Airport |  | US | 1990 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1806 |
| 8 | Zurich Airport |  | CH | 1747 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1726 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1523 |
| 12 | El Dorado International Airport |  | CO | 1503 |
| 13 | Frankfurt am Main International Airport |  | DE | 1487 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1477 |
| 16 | Macau International Airport |  | MO | 1384 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1378 |
| 18 | Congonhas Airport |  | BR | 1355 |
| 19 | Madrid Barajas International Airport |  | ES | 1294 |
| 20 | Capua Airport |  | IT | 1286 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1252 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1160 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Kuala Lumpur International Airport |  | MY | 1119 |
| 26 | Charles de Gaulle International Airport |  | FR | 1116 |
| 27 | Malpensa International Airport |  | IT | 1084 |
| 28 | Bengaluru International Airport |  | IN | 1071 |
| 29 | Ninoy Aquino International Airport |  | PH | 1012 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1007 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 32 | Barcelona International Airport |  | ES | 970 |
| 33 | Daniel K Inouye International Airport |  | US | 959 |
| 34 | Seattle-Tacoma International Airport |  | US | 951 |
| 35 | Calgary International Airport |  | CA | 937 |
| 36 | Viracopos International Airport |  | BR | 930 |
| 37 | Scottsdale Airport |  | US | 917 |
| 38 | Tenerife Norte Airport |  | ES | 914 |
| 39 | Oslo Gardermoen Airport |  | NO | 913 |
| 40 | Reno/Tahoe International Airport |  | US | 902 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 597 | 21m | 244 km | 2,513.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 394 | 24m | 225 km | 1,528.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 305 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 244 | 22m | 55 km | 231.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 225 | 1h 47m | 1,423 km | 5,521.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 210 | 20m | 250 km | 907.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 208 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 195 | 1h 15m | 961 km | 3,232.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 192 | 18m | 144 km | 477.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 183 | 1h 39m | 1,156 km | 3,650.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WMT9984 | WMT | Budapest Ferenc Liszt International Airport (LHBP) | Malpensa International Airport (LIMC) | 2026-08-01 06:59 UTC | 2026-08-01 08:20 UTC | 1h 20m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-01 07:57 UTC | 2026-08-01 08:08 UTC | 11m |
| MMA505 | MMA | Yangon International Airport (VYYY) | Yangon International Airport (VYYY) | 2026-08-01 07:53 UTC | 2026-08-01 08:03 UTC | 10m |
| N364EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-01 04:56 UTC | 2026-08-01 08:02 UTC | 3h 5m |
| HAF403 | HAF | Elefsis Airport (LGEL) | Kasteli Airport (LGTL) | 2026-08-01 07:29 UTC | 2026-08-01 07:59 UTC | 29m |
| THY1SL | Turkish Airlines | Istanbul Airport (LTFM) | Pushkin Airport (ULLP) | 2026-08-01 05:26 UTC | 2026-08-01 07:58 UTC | 2h 31m |
| CMA574 | CMA | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-07-31 20:53 UTC | 2026-08-01 07:56 UTC | 11h 3m |
| SEJYV | SEJ | Raron Airport (LSTA) | Muenster Aero Airport (LSPU) | 2026-08-01 07:41 UTC | 2026-08-01 07:56 UTC | 14m |
| LDX11C | LDX | Cascais Airport (LPCS) | Lisbon Portela Airport (LPPT) | 2026-08-01 07:39 UTC | 2026-08-01 07:52 UTC | 13m |
| CKS231 | CKS | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-07-31 20:56 UTC | 2026-08-01 07:50 UTC | 10h 54m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-07-31 21:00 UTC | 2026-08-01 07:48 UTC | 10h 48m |
| HBETX | HBE | Lommis Airfield (LSZT) | Lommis Airfield (LSZT) | 2026-08-01 07:31 UTC | 2026-08-01 07:43 UTC | 12m |
| HBZPV | HBZ | Speck-Fehraltorf Airport (LSZK) | LSMF (LSMF) | 2026-08-01 07:13 UTC | 2026-08-01 07:40 UTC | 26m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-07-31 20:28 UTC | 2026-08-01 07:39 UTC | 11h 11m |
| MEA245 | Middle East Airlines | Z19O (Z19O) | Cengiz Topel Airport (LTBQ) | 2026-08-01 06:28 UTC | 2026-08-01 07:32 UTC | 1h 4m |
| OAL038 | OAL | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-08-01 07:11 UTC | 2026-08-01 07:29 UTC | 17m |
| AAH550 | AAH | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Upolu Airport (PHUP) | 2026-08-01 07:15 UTC | 2026-08-01 07:28 UTC | 13m |
| AIQ3142 | AIQ | Don Mueang International Airport (VTBD) | Kawthoung Airport (VYKT) | 2026-08-01 06:45 UTC | 2026-08-01 07:27 UTC | 42m |
| UBG149 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-01 06:55 UTC | 2026-08-01 07:26 UTC | 31m |
| SCQZ4H | SCQ | Gullknapp Flpl Airport (ENGK) | Kristiansand Airport (ENCN) | 2026-08-01 07:07 UTC | 2026-08-01 07:26 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
