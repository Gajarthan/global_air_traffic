# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_21:16:52_UTC-green)

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

**2026-03-28 21:16:52 UTC**

- **9,840** aircraft tracked
- **9,034** currently in the air
- **806** on the ground
- **98** countries
- **100** airports with traffic
- **50** airlines identified
- **160** flight routes (last 2h)
- **1h 21m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Delta Air Lines | 455 |
| 2 | Southwest Airlines | 450 |
| 3 | United Airlines | 437 |
| 4 | American Airlines | 428 |
| 5 | Ryanair | 326 |
| 6 | SkyWest Airlines | 214 |
| 7 | EJA | 144 |
| 8 | JetBlue | 128 |
| 9 | Republic Airways | 123 |
| 10 | Alaska Airlines | 105 |
| 11 | easyJet | 101 |
| 12 | Lufthansa | 97 |
| 13 | Air Canada | 94 |
| 14 | FFT | 92 |
| 15 | ENY | 86 |
| 16 | WJA | 76 |
| 17 | LXJ | 72 |
| 18 | EJU | 70 |
| 19 | AAY | 70 |
| 20 | KLM Royal Dutch | 67 |
| 21 | Air France | 62 |
| 22 | EDV | 54 |
| 23 | NKS | 53 |
| 24 | JIA | 53 |
| 25 | Vueling | 48 |
| 26 | EXS | 47 |
| 27 | Scandinavian Airlines | 45 |
| 28 | CXK | 44 |
| 29 | Turkish Airlines | 44 |
| 30 | LATAM Airlines | 43 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 6363 |
| 2 | 🇨🇦 Canada | 430 |
| 3 | 🇬🇧 United Kingdom | 263 |
| 4 | 🇮🇪 Ireland | 246 |
| 5 | 🇩🇪 Germany | 173 |
| 6 | 🇦🇺 Australia | 163 |
| 7 | 🇪🇸 Spain | 146 |
| 8 | 🏳️ Malta | 137 |
| 9 | 🇹🇷 Turkey | 133 |
| 10 | 🇲🇽 Mexico | 125 |
| 11 | 🇧🇷 Brazil | 113 |
| 12 | 🇫🇷 France | 112 |
| 13 | 🇨🇳 China | 109 |
| 14 | 🏳️ Kingdom of the Netherlands | 91 |
| 15 | 🇦🇹 Austria | 89 |
| 16 | 🏳️ Republic of Korea | 68 |
| 17 | 🇦🇪 United Arab Emirates | 65 |
| 18 | 🇨🇭 Switzerland | 63 |
| 19 | 🇵🇱 Poland | 59 |
| 20 | 🇸🇪 Sweden | 56 |
| 21 | 🇮🇳 India | 51 |
| 22 | 🇳🇿 New Zealand | 47 |
| 23 | 🇯🇵 Japan | 44 |
| 24 | 🇸🇬 Singapore | 40 |
| 25 | 🏳️ Hungary | 39 |
| 26 | 🇹🇭 Thailand | 38 |
| 27 | 🇵🇹 Portugal | 38 |
| 28 | 🇨🇱 Chile | 29 |
| 29 | 🇳🇴 Norway | 29 |
| 30 | 🇹🇼 Taiwan | 26 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Sydney Kingsford Smith International Airport | Sydney | AU | 27 |
| 2 | General Edward Lawrence Logan International Airport | Boston | US | 23 |
| 3 | Orlando International Airport | Orlando | US | 23 |
| 4 | Toronto Pearson International Airport | Mississauga | CA | 22 |
| 5 | Washington Dulles International Airport | Washington | US | 20 |
| 6 | Ronald Reagan Washington Ntl Airport | Washington | US | 20 |
| 7 | Cancun International Airport | Cancun | MX | 19 |
| 8 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 18 |
| 9 | Harry Reid International Airport | Las Vegas | US | 18 |
| 10 | Zurich Airport | Zurich | CH | 17 |
| 11 | Phoenix Sky Harbor International Airport | Phoenix | US | 16 |
| 12 | Chicago O'Hare International Airport | Chicago | US | 16 |
| 13 | Los Angeles International Airport | Los Angeles | US | 15 |
| 14 | Newark Liberty International Airport | Newark | US | 14 |
| 15 | Seattle-Tacoma International Airport | Seattle | US | 14 |
| 16 | Laguardia Airport | New York | US | 13 |
| 17 | El Dorado International Airport | Bogota | CO | 13 |
| 18 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 13 |
| 19 | John F Kennedy International Airport | New York | US | 13 |
| 20 | Melbourne International Airport | Melbourne | AU | 13 |
| 21 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 11 |
| 22 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 11 |
| 23 | Nashville International Airport | Nashville | US | 10 |
| 24 | San Francisco International Airport | San Francisco | US | 10 |
| 25 | Calgary International Airport | Calgary | CA | 10 |
| 26 | Vancouver International Airport | Richmond | CA | 10 |
| 27 | Tampa International Airport | Tampa | US | 9 |
| 28 | Rocky Mountain Metro Airport | Denver | US | 9 |
| 29 | Northern Colorado Regional Airport | Fort Collins/Loveland | US | 8 |
| 30 | Austin-Bergstrom International Airport | Austin | US | 8 |
| 31 | Oakland San Francisco Bay Airport | Oakland | US | 8 |
| 32 | Chek Lap Kok International Airport | Hong Kong | HK | 8 |
| 33 | Salt Lake City International Airport | Salt Lake City | US | 7 |
| 34 | Manchester Airport | Manchester | GB | 7 |
| 35 | Paris-Orly Airport | Paris | FR | 6 |
| 36 | Malpensa International Airport | Milan | IT | 6 |
| 37 | Indira Gandhi International Airport | New Delhi | IN | 6 |
| 38 | General Mariano Escobedo International Airport | Monterrey | MX | 6 |
| 39 | Chhatrapati Shivaji International Airport | Mumbai | IN | 6 |
| 40 | Narita International Airport | Tokyo | JP | 6 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2 | 32m |
| 2 | Miami-Opa Locka Executive Airport (KOPF) | Reno/Tahoe International Airport (KRNO) | 2 | 5h 16m |
| 3 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2 | 20m |
| 4 | KU42 (KU42) | Wendover Airport (KENV) | 2 | 48m |
| 5 | Athanasiou Valley Airport (CO07) | Athanasiou Valley Airport (CO07) | 2 | 20m |
| 6 | Scottsdale Airport (KSDL) | Rimrock Airport (48AZ) | 2 | 22m |
| 7 | Charles de Gaulle International Airport (LFPG) | Mostaganem Airport (DA14) | 1 | 1h 47m |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 1 | 15m |
| 9 | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 1 | 24m |
| 10 | Santa Cruz del Quiche Airport (MGQC) | La Aurora Airport (MGGT) | 1 | 28m |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 1 | 21m |
| 12 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 1 | 19m |
| 13 | Xoxocotlan International Airport (MMOX) | Atizapan De Zaragoza Airport (MMJC) | 1 | 42m |
| 14 | Francisco Sarabia International Airport (MMTC) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 4m |
| 15 | Hermanos Serdan International Airport (MMPB) | General Mariano Matamoros Airport (MMCB) | 1 | 16m |
| 16 | Palma De Mallorca Airport (LEPA) | Leon Airport (LELN) | 1 | 1h 7m |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 1 | 33m |
| 18 | Sevilla Airport (LEZL) | Lanzarote Airport (GCRR) | 1 | 1h 30m |
| 19 | Glasgow International Airport (EGPF) | Glasgow International Airport (EGPF) | 1 | 3m |
| 20 | Manchester Airport (EGCC) | Tenerife Norte Airport (GCXO) | 1 | 3h 48m |
| 21 | East Midlands Airport (EGNX) | La Gomera Airport (GCGM) | 1 | 3h 30m |
| 22 | London Gatwick Airport (EGKK) | Castellón De La Plana Airport (LECN) | 1 | 1h 35m |
| 23 | Oslo Gardermoen Airport (ENGM) | Pristina International Airport (BKPR) | 1 | 2h 41m |
| 24 | Warsaw Chopin Airport (EPWA) | Malpensa International Airport (LIMC) | 1 | 1h 48m |
| 25 | Copernicus Wrocław Airport (EPWR) | Newcastle Airport (EGNT) | 1 | 1h 49m |
| 26 | Paris Beauvais Tille Airport (LFOB) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 1 | 1h 50m |
| 27 | Geneva Cointrin International Airport (LSGG) | Brussels Airport (EBBR) | 1 | 55m |
| 28 | Adnan Menderes International Airport (LTBJ) | Adana Airport (LTAF) | 1 | 53m |
| 29 | London Luton Airport (EGGW) | Karain Airport (LTXE) | 1 | 3h 31m |
| 30 | London Luton Airport (EGGW) | EPCH (EPCH) | 1 | 1h 38m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| REH13 | REH | Hesperia Airport (KL26) | On The Rocks Airport (1CA6) | 2026-03-28 20:20 UTC | 2026-03-28 21:05 UTC | 45m |
| N491LG |  | Athanasiou Valley Airport (CO07) | Athanasiou Valley Airport (CO07) | 2026-03-28 20:44 UTC | 2026-03-28 20:54 UTC | 10m |
| CWA809 | CWA | Edmonton International Airport (CYEG) | Bawlf (Blackwells) Airport (CFR2) | 2026-03-28 20:24 UTC | 2026-03-28 20:46 UTC | 21m |
| CXK525 | CXK | New Braunfels Ntl Airport (KBAZ) | New Braunfels Ntl Airport (KBAZ) | 2026-03-28 20:44 UTC | 2026-03-28 20:46 UTC | 1m |
| TGCYC | TGC | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-03-28 20:24 UTC | 2026-03-28 20:45 UTC | 21m |
| N115RP |  | Midland International Air And Space Port Airport (KMAF) | Andrews County Airport (KE11) | 2026-03-28 20:29 UTC | 2026-03-28 20:41 UTC | 12m |
| N621N |  | KFTG (KFTG) | High Plains Airport Airport (CD15) | 2026-03-28 20:28 UTC | 2026-03-28 20:40 UTC | 12m |
| RYR10RA | Ryanair | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 2026-03-28 19:24 UTC | 2026-03-28 20:30 UTC | 1h 5m |
| N528TH |  | Addison Airport (KADS) | 0TX8 (0TX8) | 2026-03-28 19:41 UTC | 2026-03-28 20:29 UTC | 48m |
| N8488M |  | Carson City Airport (KCXP) | Dayton Valley Airpark (KA34) | 2026-03-28 20:02 UTC | 2026-03-28 20:27 UTC | 24m |
| N322ME |  | Veterans Airport Of Southern Illinois Airport (KMWA) | Herrington Field (42MD) | 2026-03-28 18:47 UTC | 2026-03-28 20:26 UTC | 1h 39m |
| WSN3 | WSN | Albuquerque International Sunport Airport (KABQ) | Grant County Airport (KSVC) | 2026-03-28 19:43 UTC | 2026-03-28 20:24 UTC | 41m |
| N6261R |  | Montgomery-Gibbs Executive Airport (KMYF) | Big Bear City Airport (KL35) | 2026-03-28 19:33 UTC | 2026-03-28 20:23 UTC | 49m |
| BYF31 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-03-28 19:45 UTC | 2026-03-28 20:22 UTC | 36m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-03-28 19:54 UTC | 2026-03-28 20:22 UTC | 27m |
| SWA3300 | Southwest Airlines | Evans Aerodrome (XS39) | San Antonio International Airport (KSAT) | 2026-03-28 19:43 UTC | 2026-03-28 20:20 UTC | 36m |
| N6440J |  | Northwest Alabama Regional Airport (KMSL) | Wilson Creek Airport (0AL9) | 2026-03-28 20:08 UTC | 2026-03-28 20:19 UTC | 11m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-03-28 06:10 UTC | 2026-03-28 20:18 UTC | 14h 8m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-28 05:56 UTC | 2026-03-28 20:17 UTC | 14h 21m |
| N565JP |  | Henderson Executive Airport (KHND) | Creekside Airport (03XS) | 2026-03-28 18:17 UTC | 2026-03-28 20:17 UTC | 1h 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
