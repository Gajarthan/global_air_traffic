# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_23:53:03_UTC-green)

![Flight Map](images/flight_map.png)

## About

Real-time tracking of global air traffic using the [OpenSky Network](https://opensky-network.org/) API. This repository automatically fetches live aircraft positions worldwide and generates visualizations and statistics.

**Data Source:** OpenSky Network REST API (`/states/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches all aircraft transponder data globally
- Maps on-ground aircraft to nearest airports (28,000+ airport database)
- Identifies airlines from ICAO callsign prefixes
- Generates a live flight map and summary statistics

## Live Snapshot

**2026-03-28 23:53:03 UTC**

- **7,531** aircraft tracked
- **6,813** currently in the air
- **718** on the ground
- **88** countries
- **100** airports with traffic
- **50** airlines identified
- **121** flight routes (last 2h)
- **1h 18m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | American Airlines | 494 |
| 2 | United Airlines | 477 |
| 3 | Southwest Airlines | 458 |
| 4 | Delta Air Lines | 422 |
| 5 | SkyWest Airlines | 188 |
| 6 | JetBlue | 130 |
| 7 | Alaska Airlines | 116 |
| 8 | FFT | 98 |
| 9 | Air Canada | 96 |
| 10 | ENY | 93 |
| 11 | Republic Airways | 82 |
| 12 | EJA | 72 |
| 13 | AAY | 69 |
| 14 | Turkish Airlines | 62 |
| 15 | Ryanair | 60 |
| 16 | WJA | 58 |
| 17 | All Nippon Airways | 53 |
| 18 | NKS | 52 |
| 19 | Japan Airlines | 49 |
| 20 | IndiGo | 47 |
| 21 | easyJet | 44 |
| 22 | LATAM Airlines | 42 |
| 23 | JIA | 41 |
| 24 | Virgin Australia | 41 |
| 25 | ANZ | 40 |
| 26 | JST | 40 |
| 27 | British Airways | 37 |
| 28 | LXJ | 35 |
| 29 | Qantas | 35 |
| 30 | SCX | 34 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 4931 |
| 2 | 🇨🇦 Canada | 349 |
| 3 | 🇦🇺 Australia | 306 |
| 4 | 🇯🇵 Japan | 179 |
| 5 | 🇬🇧 United Kingdom | 164 |
| 6 | 🇹🇷 Turkey | 126 |
| 7 | 🇨🇳 China | 112 |
| 8 | 🇲🇽 Mexico | 111 |
| 9 | 🇮🇳 India | 86 |
| 10 | 🏳️ Republic of Korea | 85 |
| 11 | 🇧🇷 Brazil | 83 |
| 12 | 🇮🇪 Ireland | 74 |
| 13 | 🇳🇿 New Zealand | 71 |
| 14 | 🇹🇼 Taiwan | 52 |
| 15 | 🇩🇪 Germany | 51 |
| 16 | 🇪🇸 Spain | 41 |
| 17 | 🇦🇪 United Arab Emirates | 41 |
| 18 | 🇫🇷 France | 41 |
| 19 | 🇮🇩 Indonesia | 39 |
| 20 | 🇵🇭 Philippines | 39 |
| 21 | 🇨🇱 Chile | 31 |
| 22 | 🇸🇬 Singapore | 31 |
| 23 | 🇲🇾 Malaysia | 30 |
| 24 | 🏳️ Malta | 30 |
| 25 | 🇪🇬 Egypt | 27 |
| 26 | 🏳️ Kingdom of the Netherlands | 26 |
| 27 | 🇹🇭 Thailand | 25 |
| 28 | 🇸🇦 Saudi Arabia | 19 |
| 29 | 🏳️ Russian Federation | 18 |
| 30 | 🏳️ Panama | 18 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 43 |
| 2 | Denver International Airport | Denver | US | 30 |
| 3 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 26 |
| 4 | Orlando International Airport | Orlando | US | 24 |
| 5 | Sydney Kingsford Smith International Airport | Sydney | AU | 24 |
| 6 | John F Kennedy International Airport | New York | US | 22 |
| 7 | Tokyo International Airport | Tokyo | JP | 21 |
| 8 | Toronto Pearson International Airport | Mississauga | CA | 20 |
| 9 | General Edward Lawrence Logan International Airport | Boston | US | 19 |
| 10 | Chicago O'Hare International Airport | Chicago | US | 17 |
| 11 | San Francisco International Airport | San Francisco | US | 17 |
| 12 | Nashville International Airport | Nashville | US | 16 |
| 13 | Chek Lap Kok International Airport | Hong Kong | HK | 15 |
| 14 | Cancun International Airport | Cancun | MX | 15 |
| 15 | Indira Gandhi International Airport | New Delhi | IN | 14 |
| 16 | Phoenix Sky Harbor International Airport | Phoenix | US | 14 |
| 17 | Harry Reid International Airport | Las Vegas | US | 14 |
| 18 | Vancouver International Airport | Richmond | CA | 14 |
| 19 | Newark Liberty International Airport | Newark | US | 12 |
| 20 | Melbourne International Airport | Melbourne | AU | 10 |
| 21 | Calgary International Airport | Calgary | CA | 10 |
| 22 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 9 |
| 23 | Southwest Florida International Airport | Fort Myers | US | 9 |
| 24 | Los Angeles International Airport | Los Angeles | US | 9 |
| 25 | El Dorado International Airport | Bogota | CO | 8 |
| 26 | St Louis Lambert International Airport | St Louis | US | 8 |
| 27 | Salt Lake City International Airport | Salt Lake City | US | 8 |
| 28 | Laguardia Airport | New York | US | 7 |
| 29 | Tampa International Airport | Tampa | US | 7 |
| 30 | Norman Y Mineta San Jose International Airport | San Jose | US | 7 |
| 31 | Washington Dulles International Airport | Washington | US | 6 |
| 32 | Perth International Airport | Perth | AU | 6 |
| 33 | Santa Monica Municipal Airport | Santa Monica | US | 5 |
| 34 | Ronald Reagan Washington Ntl Airport | Washington | US | 5 |
| 35 | Oakland San Francisco Bay Airport | Oakland | US | 5 |
| 36 | Ted Stevens Anchorage International Airport | Anchorage | US | 5 |
| 37 | Chhatrapati Shivaji International Airport | Mumbai | IN | 5 |
| 38 | Brisbane International Airport | Brisbane | AU | 5 |
| 39 | Palo Alto Airport | Palo Alto | US | 5 |
| 40 | Brisbane Archerfield Airport | Brisbane | AU | 4 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 2 | 1h 56m |
| 2 | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2 | 1h 8m |
| 3 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2 | 18m |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1 | 14m |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 1 | 23m |
| 6 | La Aurora Airport (MGGT) | La America Airport (MHEI) | 1 | 40m |
| 7 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 1 | 38m |
| 8 | Abraham Gonzalez International Airport (MMCS) | Atizapan De Zaragoza Airport (MMJC) | 1 | 2h 0m |
| 9 | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 1 | 25m |
| 10 | Chhatrapati Shivaji International Airport (VABB) | Malpensa International Airport (LIMC) | 1 | 11h 24m |
| 11 | Samsun Samair Airport (LTAQ) | Samsun Samair Airport (LTAQ) | 1 | 0m |
| 12 | Brussels South Charleroi Airport (EBCI) | Tenerife Norte Airport (GCXO) | 1 | 3h 38m |
| 13 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 1 | 23m |
| 14 | VGZR (VGZR) | Macau International Airport (VMMC) | 1 | 2h 40m |
| 15 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 1 | 11h 34m |
| 16 | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 1 | 11h 34m |
| 17 | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 1 | 32m |
| 18 | Toowoomba Wellcamp Airport (YBWW) | Ballina Byron Gateway Airport (YBNA) | 1 | 1h 25m |
| 19 | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 1 | 35m |
| 20 | Sydney Kingsford Smith International Airport (YSSY) | Avalon Airport (YMAV) | 1 | 1h 6m |
| 21 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 1 | 38m |
| 22 | Soekarno-Hatta International Airport (WIII) | Tunggul Wulung Airport (WIHL) | 1 | 26m |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 1 | 21m |
| 24 | Albuquerque International Sunport Airport (KABQ) | Telluride Regional Airport (KTEX) | 1 | 25m |
| 25 | Salt Lake City International Airport (KSLC) | Norman Y Mineta San Jose International Airport (KSJC) | 1 | 1h 26m |
| 26 | Krey Field (0CL1) | Gray Butte Field (04CA) | 1 | 36m |
| 27 | Addison Airport (KADS) | Manassas Regional/Harry P Davis Field (KHEF) | 1 | 2h 14m |
| 28 | Milhous Ranch Airport (79CL) | Milhous Ranch Airport (79CL) | 1 | 2h 0m |
| 29 | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Wichita Dwight D Eisenhower Ntl Airport (KICT) | 1 | 1h 4m |
| 30 | Julian Hinds Pump Plant Airstrip (73CL) | Henderson Executive Airport (KHND) | 1 | 27m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N15ED |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Wichita Dwight D Eisenhower Ntl Airport (KICT) | 2026-03-28 22:37 UTC | 2026-03-28 23:42 UTC | 1h 4m |
| N133TH |  | Milhous Ranch Airport (79CL) | Milhous Ranch Airport (79CL) | 2026-03-28 21:32 UTC | 2026-03-28 23:32 UTC | 2h 0m |
| CXK1073 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-03-28 21:50 UTC | 2026-03-28 23:27 UTC | 1h 37m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-03-28 11:42 UTC | 2026-03-28 23:17 UTC | 11h 34m |
| N7830T |  | Petes Airpark (8OL1) | Gregg Airport (7OK1) | 2026-03-28 22:50 UTC | 2026-03-28 23:17 UTC | 26m |
| LT617 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-03-28 22:19 UTC | 2026-03-28 23:11 UTC | 51m |
| TKJ5QY | TKJ | Samsun Samair Airport (LTAQ) | Samsun Samair Airport (LTAQ) | 2026-03-28 23:08 UTC | 2026-03-28 23:08 UTC | 0m |
| N680SF |  | John F Kennedy International Airport (KJFK) | Akron-Canton Regional Airport (KCAK) | 2026-03-28 21:53 UTC | 2026-03-28 23:04 UTC | 1h 11m |
| BYF43 | BYF | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-03-28 22:31 UTC | 2026-03-28 23:02 UTC | 31m |
| N103UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-03-28 22:40 UTC | 2026-03-28 23:01 UTC | 21m |
| N6502W |  | Cincinnati Municipal/Lunken Field (KLUK) | Indianapolis Executive Airport (KTYQ) | 2026-03-28 21:53 UTC | 2026-03-28 23:00 UTC | 1h 6m |
| N5107H |  | Green Mountain Airport (WA67) | Scappoose Airport (KSPB) | 2026-03-28 22:34 UTC | 2026-03-28 22:59 UTC | 25m |
| N806MC |  | Mc Clellan-Palomar Airport (KCRQ) | Swains Creek Airport (UT00) | 2026-03-28 22:13 UTC | 2026-03-28 22:58 UTC | 44m |
| N120PV |  | Krey Field (0CL1) | Gray Butte Field (04CA) | 2026-03-28 22:21 UTC | 2026-03-28 22:58 UTC | 36m |
| N537TW |  | Mckinney Ntl Airport (KTKI) | 0TX8 (0TX8) | 2026-03-28 22:16 UTC | 2026-03-28 22:56 UTC | 40m |
| ZKRXD | ZKR | Napier Airport (NZNR) | Queenstown International Airport (NZQN) | 2026-03-28 21:27 UTC | 2026-03-28 22:52 UTC | 1h 25m |
| N6090F |  | Addison Airport (KADS) | Jlinn Airport (37TS) | 2026-03-28 21:40 UTC | 2026-03-28 22:52 UTC | 1h 12m |
| ENY3979 | ENY | Dallas-Fort Worth International Airport (KDFW) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-03-28 22:09 UTC | 2026-03-28 22:50 UTC | 40m |
| N64WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-03-28 22:10 UTC | 2026-03-28 22:50 UTC | 39m |
| N29WB |  | Gnoss Field (KDVO) | CL36 (CL36) | 2026-03-28 21:56 UTC | 2026-03-28 22:48 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
