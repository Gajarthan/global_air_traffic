# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_04:45:09_UTC-green)

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

**2026-03-29 04:45:09 UTC**

- **4,897** aircraft tracked
- **4,307** currently in the air
- **590** on the ground
- **91** countries
- **100** airports with traffic
- **50** airlines identified
- **66** flight routes (last 2h)
- **1h 16m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Southwest Airlines | 256 |
| 2 | Ryanair | 226 |
| 3 | American Airlines | 191 |
| 4 | Delta Air Lines | 141 |
| 5 | United Airlines | 125 |
| 6 | Lufthansa | 93 |
| 7 | Alaska Airlines | 86 |
| 8 | IndiGo | 77 |
| 9 | Turkish Airlines | 72 |
| 10 | FFT | 69 |
| 11 | KLM Royal Dutch | 64 |
| 12 | SkyWest Airlines | 61 |
| 13 | Air France | 59 |
| 14 | Air Canada | 54 |
| 15 | JetBlue | 53 |
| 16 | Air India | 52 |
| 17 | All Nippon Airways | 50 |
| 18 | Wizz Air | 46 |
| 19 | Cathay Pacific | 44 |
| 20 | Virgin Australia | 43 |
| 21 | Japan Airlines | 42 |
| 22 | WMT | 40 |
| 23 | British Airways | 39 |
| 24 | Finnair | 39 |
| 25 | WJA | 38 |
| 26 | Scandinavian Airlines | 37 |
| 27 | Qantas | 37 |
| 28 | EJU | 35 |
| 29 | JST | 34 |
| 30 | NKS | 33 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 1649 |
| 2 | 🇦🇺 Australia | 296 |
| 3 | 🇨🇳 China | 242 |
| 4 | 🇨🇦 Canada | 187 |
| 5 | 🇯🇵 Japan | 167 |
| 6 | 🇮🇳 India | 164 |
| 7 | 🇮🇪 Ireland | 162 |
| 8 | 🇩🇪 Germany | 160 |
| 9 | 🇹🇷 Turkey | 152 |
| 10 | 🏳️ Malta | 115 |
| 11 | 🇫🇷 France | 87 |
| 12 | 🏳️ Republic of Korea | 87 |
| 13 | 🇬🇧 United Kingdom | 82 |
| 14 | 🏳️ Kingdom of the Netherlands | 73 |
| 15 | 🇲🇽 Mexico | 72 |
| 16 | 🇵🇱 Poland | 59 |
| 17 | 🏳️ Hungary | 58 |
| 18 | 🇪🇸 Spain | 54 |
| 19 | 🇨🇭 Switzerland | 54 |
| 20 | 🇹🇼 Taiwan | 53 |
| 21 | 🇦🇹 Austria | 52 |
| 22 | 🇹🇭 Thailand | 50 |
| 23 | 🇳🇿 New Zealand | 49 |
| 24 | 🇦🇪 United Arab Emirates | 43 |
| 25 | 🇲🇾 Malaysia | 42 |
| 26 | 🇮🇩 Indonesia | 39 |
| 27 | 🇸🇬 Singapore | 39 |
| 28 | 🇫🇮 Finland | 37 |
| 29 | 🏳️ Greece | 35 |
| 30 | 🇸🇪 Sweden | 30 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Sydney Kingsford Smith International Airport | Sydney | AU | 23 |
| 2 | Toronto Pearson International Airport | Mississauga | CA | 21 |
| 3 | San Francisco International Airport | San Francisco | US | 21 |
| 4 | Los Angeles International Airport | Los Angeles | US | 19 |
| 5 | Tokyo International Airport | Tokyo | JP | 19 |
| 6 | Zurich Airport | Zurich | CH | 17 |
| 7 | Chek Lap Kok International Airport | Hong Kong | HK | 15 |
| 8 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 14 |
| 9 | Denver International Airport | Denver | US | 14 |
| 10 | Phoenix Sky Harbor International Airport | Phoenix | US | 13 |
| 11 | Seattle-Tacoma International Airport | Seattle | US | 13 |
| 12 | Netaji Subhash Chandra Bose International Airport | Kolkata | IN | 11 |
| 13 | Harry Reid International Airport | Las Vegas | US | 10 |
| 14 | Austin-Bergstrom International Airport | Austin | US | 10 |
| 15 | Amsterdam Airport Schiphol | Amsterdam | NL | 10 |
| 16 | El Dorado International Airport | Bogota | CO | 9 |
| 17 | Eleftherios Venizelos International Airport | Athens | GR | 9 |
| 18 | Orlando International Airport | Orlando | US | 9 |
| 19 | Paris-Orly Airport | Paris | FR | 9 |
| 20 | General Edward Lawrence Logan International Airport | Boston | US | 9 |
| 21 | Melbourne International Airport | Melbourne | AU | 9 |
| 22 | Narita International Airport | Tokyo | JP | 9 |
| 23 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 9 |
| 24 | Vancouver International Airport | Richmond | CA | 9 |
| 25 | San Diego International Airport | San Diego | US | 8 |
| 26 | Calgary International Airport | Calgary | CA | 8 |
| 27 | Ted Stevens Anchorage International Airport | Anchorage | US | 8 |
| 28 | Indira Gandhi International Airport | New Delhi | IN | 7 |
| 29 | Vienna International Airport | Vienna | AT | 7 |
| 30 | Thessaloniki Macedonia International Airport | Thessaloniki | GR | 7 |
| 31 | Chicago O'Hare International Airport | Chicago | US | 6 |
| 32 | Malpensa International Airport | Milan | IT | 6 |
| 33 | Melbourne Moorabbin Airport | Melbourne | AU | 5 |
| 34 | Norman Y Mineta San Jose International Airport | San Jose | US | 5 |
| 35 | Chhatrapati Shivaji International Airport | Mumbai | IN | 5 |
| 36 | Dhaka / Hazrat Shahjalal International Airport | Dhaka | BD | 5 |
| 37 | Helsinki Vantaa Airport | Helsinki | FI | 5 |
| 38 | London Gatwick Airport | London | GB | 5 |
| 39 | Kaohsiung International Airport | Kaohsiung City | TW | 5 |
| 40 | Manchester Airport | Manchester | GB | 5 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 2 | 14m |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2 | 22m |
| 3 | Albury Airport (YMAY) | Albury Airport (YMAY) | 2 | 16m |
| 4 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2 | 21m |
| 5 | Incheon International Airport (RKSI) | Takamatsu Airport (RJOT) | 1 | 1h 4m |
| 6 | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 1 | 20m |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 1 | 16m |
| 8 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 1 | 29m |
| 9 | Diosdado Macapagal International Airport (RPLC) | Wasig Airport (RPVL) | 1 | 32m |
| 10 | Suvarnabhumi Airport (VTBS) | Macau International Airport (VMMC) | 1 | 9h 23m |
| 11 | Pechora Airport (UUYP) | Takamatsu Airport (RJOT) | 1 | 10h 18m |
| 12 | Nagasaki Airport (RJFU) | Takamatsu Airport (RJOT) | 1 | 25m |
| 13 | Chek Lap Kok International Airport (VHHH) | Shek Kong Air Base (VHSK) | 1 | 39m |
| 14 | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 1 | 45m |
| 15 | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 1 | 19m |
| 16 | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 1 | 14m |
| 17 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 1 | 36m |
| 18 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 1 | 39m |
| 19 | Sunshine Coast Airport (YBMC) | Sydney Kingsford Smith International Airport (YSSY) | 1 | 1h 14m |
| 20 | Gold Coast Airport (YBCG) | Braidwood Airport (YBAO) | 1 | 1h 9m |
| 21 | Newcastle Airport (YWLM) | Armidale Airport (YARM) | 1 | 34m |
| 22 | Brisbane International Airport (YBBN) | Queenstown International Airport (NZQN) | 1 | 2h 42m |
| 23 | Sydney Kingsford Smith International Airport (YSSY) | Grenfell Airport (YGNF) | 1 | 33m |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 1 | 1h 38m |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Kailashahar Airport (VEKR) | 1 | 31m |
| 26 | Juhu Aerodrome (VAJJ) | Tirupati Airport (VOTP) | 1 | 1h 12m |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Bengaluru International Airport (VOBL) | 1 | 2h 6m |
| 28 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 1 | 1h 42m |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Purnea Airport (VEPU) | 1 | 32m |
| 30 | Indira Gandhi International Airport (VIDP) | Udhampur Air Force Station (VIUX) | 1 | 51m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LT617 |  | San Clemente Island Nalf Airport (KNUC) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-03-29 01:56 UTC | 2026-03-29 04:21 UTC | 2h 25m |
| N359EV |  | Mcgahan Industrial Airpark (AK73) | Drift River Airport (3AK5) | 2026-03-29 04:06 UTC | 2026-03-29 04:20 UTC | 14m |
| N29CM |  | Montgomery-Gibbs Executive Airport (KMYF) | Van Nuys Airport (KVNY) | 2026-03-29 02:55 UTC | 2026-03-29 04:17 UTC | 1h 22m |
| DAL158 | Delta Air Lines | Incheon International Airport (RKSI) | Tokyo International Airport (RJTT) | 2026-03-29 01:30 UTC | 2026-03-29 04:11 UTC | 2h 41m |
| N550RL |  | Springfield-Branson Ntl Airport (KSGF) | 0AR1 (0AR1) | 2026-03-29 03:47 UTC | 2026-03-29 04:08 UTC | 21m |
| N326AF |  | Seattle Paine Field International Airport (KPAE) | Sanderson Field (KSHN) | 2026-03-29 03:23 UTC | 2026-03-29 04:02 UTC | 38m |
| N741SM |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-03-29 02:46 UTC | 2026-03-29 03:55 UTC | 1h 9m |
| CFH24 | CFH | Newcastle Airport (YWLM) | Armidale Airport (YARM) | 2026-03-29 03:07 UTC | 2026-03-29 03:42 UTC | 34m |
| CES5015 | China Eastern | Suvarnabhumi Airport (VTBS) | Macau International Airport (VMMC) | 2026-03-28 18:17 UTC | 2026-03-29 03:41 UTC | 9h 23m |
| NIJ | NIJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-03-29 03:15 UTC | 2026-03-29 03:39 UTC | 24m |
| AXM431 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-03-29 03:15 UTC | 2026-03-29 03:35 UTC | 20m |
| N2108Z |  | Mc Clellan-Palomar Airport (KCRQ) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-03-29 02:53 UTC | 2026-03-29 03:35 UTC | 41m |
|  |  | Albury Airport (YMAY) | Albury Airport (YMAY) | 2026-03-29 03:32 UTC | 2026-03-29 03:32 UTC | 0m |
| N450BG |  | Teterboro Airport (KTEB) | Van Nuys Airport (KVNY) | 2026-03-28 22:04 UTC | 2026-03-29 03:29 UTC | 5h 25m |
| VOZ1690 | Virgin Australia | Gold Coast Airport (YBCG) | Braidwood Airport (YBAO) | 2026-03-29 02:15 UTC | 2026-03-29 03:25 UTC | 1h 9m |
| APG217 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-03-29 03:00 UTC | 2026-03-29 03:23 UTC | 23m |
| QLK123D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Grenfell Airport (YGNF) | 2026-03-29 02:45 UTC | 2026-03-29 03:19 UTC | 33m |
| ANZ764L | ANZ | Christchurch International Airport (NZCH) | Hawera Airport (NZHA) | 2026-03-29 02:14 UTC | 2026-03-29 03:17 UTC | 1h 2m |
| ASA69 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Prince Rupert Airport (CYPR) | 2026-03-29 01:56 UTC | 2026-03-29 03:17 UTC | 1h 20m |
| VCI | VCI | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-29 02:35 UTC | 2026-03-29 03:15 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
