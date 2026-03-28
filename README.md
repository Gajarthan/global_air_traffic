# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_23:21:58_UTC-green)

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

**2026-03-28 23:21:58 UTC**

- **7,928** aircraft tracked
- **7,167** currently in the air
- **761** on the ground
- **91** countries
- **100** airports with traffic
- **50** airlines identified
- **134** flight routes (last 2h)
- **1h 23m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | United Airlines | 465 |
| 2 | American Airlines | 464 |
| 3 | Southwest Airlines | 452 |
| 4 | Delta Air Lines | 446 |
| 5 | SkyWest Airlines | 187 |
| 6 | JetBlue | 123 |
| 7 | Alaska Airlines | 121 |
| 8 | Ryanair | 115 |
| 9 | Air Canada | 93 |
| 10 | EJA | 89 |
| 11 | FFT | 87 |
| 12 | Republic Airways | 85 |
| 13 | ENY | 77 |
| 14 | WJA | 70 |
| 15 | AAY | 64 |
| 16 | NKS | 59 |
| 17 | easyJet | 56 |
| 18 | Japan Airlines | 54 |
| 19 | All Nippon Airways | 51 |
| 20 | LXJ | 45 |
| 21 | Turkish Airlines | 45 |
| 22 | Virgin Australia | 44 |
| 23 | EDV | 42 |
| 24 | JIA | 40 |
| 25 | Qantas | 40 |
| 26 | CXK | 38 |
| 27 | British Airways | 36 |
| 28 | SCX | 35 |
| 29 | VIV | 35 |
| 30 | LATAM Airlines | 35 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 5175 |
| 2 | 🇨🇦 Canada | 385 |
| 3 | 🇦🇺 Australia | 289 |
| 4 | 🇯🇵 Japan | 193 |
| 5 | 🇬🇧 United Kingdom | 184 |
| 6 | 🇨🇳 China | 124 |
| 7 | 🇲🇽 Mexico | 116 |
| 8 | 🇮🇪 Ireland | 111 |
| 9 | 🇹🇷 Turkey | 106 |
| 10 | 🏳️ Republic of Korea | 91 |
| 11 | 🇧🇷 Brazil | 78 |
| 12 | 🇮🇳 India | 65 |
| 13 | 🇳🇿 New Zealand | 64 |
| 14 | 🇩🇪 Germany | 62 |
| 15 | 🏳️ Malta | 62 |
| 16 | 🇪🇸 Spain | 51 |
| 17 | 🇦🇪 United Arab Emirates | 45 |
| 18 | 🇹🇼 Taiwan | 43 |
| 19 | 🇲🇾 Malaysia | 40 |
| 20 | 🇨🇱 Chile | 38 |
| 21 | 🇫🇷 France | 36 |
| 22 | 🏳️ Kingdom of the Netherlands | 31 |
| 23 | 🇵🇭 Philippines | 28 |
| 24 | 🇪🇬 Egypt | 26 |
| 25 | 🇹🇭 Thailand | 24 |
| 26 | 🇮🇩 Indonesia | 23 |
| 27 | 🇸🇬 Singapore | 21 |
| 28 | 🇵🇱 Poland | 21 |
| 29 | 🇨🇭 Switzerland | 21 |
| 30 | 🇵🇹 Portugal | 21 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 42 |
| 2 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 29 |
| 3 | Phoenix Sky Harbor International Airport | Phoenix | US | 25 |
| 4 | Sydney Kingsford Smith International Airport | Sydney | AU | 25 |
| 5 | Tokyo International Airport | Tokyo | JP | 23 |
| 6 | Chicago O'Hare International Airport | Chicago | US | 23 |
| 7 | General Edward Lawrence Logan International Airport | Boston | US | 22 |
| 8 | San Francisco International Airport | San Francisco | US | 20 |
| 9 | Toronto Pearson International Airport | Mississauga | CA | 20 |
| 10 | Orlando International Airport | Orlando | US | 20 |
| 11 | Calgary International Airport | Calgary | CA | 17 |
| 12 | Harry Reid International Airport | Las Vegas | US | 17 |
| 13 | Newark Liberty International Airport | Newark | US | 16 |
| 14 | John F Kennedy International Airport | New York | US | 14 |
| 15 | Norman Y Mineta San Jose International Airport | San Jose | US | 13 |
| 16 | Nashville International Airport | Nashville | US | 11 |
| 17 | Melbourne International Airport | Melbourne | AU | 11 |
| 18 | Vancouver International Airport | Richmond | CA | 11 |
| 19 | Denver International Airport | Denver | US | 10 |
| 20 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 10 |
| 21 | Chek Lap Kok International Airport | Hong Kong | HK | 10 |
| 22 | Southwest Florida International Airport | Fort Myers | US | 9 |
| 23 | Cancun International Airport | Cancun | MX | 9 |
| 24 | Perth International Airport | Perth | AU | 9 |
| 25 | Seattle-Tacoma International Airport | Seattle | US | 8 |
| 26 | Indira Gandhi International Airport | New Delhi | IN | 8 |
| 27 | Narita International Airport | Tokyo | JP | 8 |
| 28 | Los Angeles International Airport | Los Angeles | US | 8 |
| 29 | Tampa International Airport | Tampa | US | 8 |
| 30 | Laguardia Airport | New York | US | 8 |
| 31 | Austin-Bergstrom International Airport | Austin | US | 7 |
| 32 | San Diego International Airport | San Diego | US | 7 |
| 33 | Salt Lake City International Airport | Salt Lake City | US | 7 |
| 34 | Brisbane International Airport | Brisbane | AU | 7 |
| 35 | Zurich Airport | Zurich | CH | 7 |
| 36 | Netaji Subhash Chandra Bose International Airport | Kolkata | IN | 6 |
| 37 | Louis Armstrong New Orleans International Airport | New Orleans | US | 6 |
| 38 | General Mariano Escobedo International Airport | Monterrey | MX | 6 |
| 39 | St Louis Lambert International Airport | St Louis | US | 6 |
| 40 | Gimpo International Airport | Seoul | KR | 6 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2 | 28m |
| 2 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2 | 34m |
| 3 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 1 | 13m |
| 4 | La Aurora Airport (MGGT) | La America Airport (MHEI) | 1 | 40m |
| 5 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 52m |
| 6 | Abraham Gonzalez International Airport (MMCS) | Atizapan De Zaragoza Airport (MMJC) | 1 | 2h 0m |
| 7 | Chhatrapati Shivaji International Airport (VABB) | Malpensa International Airport (LIMC) | 1 | 11h 24m |
| 8 | London Stansted Airport (EGSS) | Frankfurt-Hahn Airport (EDFH) | 1 | 51m |
| 9 | Alicante International Airport (LEAL) | Malpensa International Airport (LIMC) | 1 | 1h 39m |
| 10 | Riga International Airport (EVRA) | Zurich Airport (LSZH) | 1 | 2h 18m |
| 11 | VGZR (VGZR) | Macau International Airport (VMMC) | 1 | 2h 40m |
| 12 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 1 | 11h 34m |
| 13 | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 1 | 32m |
| 14 | Toowoomba Wellcamp Airport (YBWW) | Ballina Byron Gateway Airport (YBNA) | 1 | 1h 25m |
| 15 | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 1 | 35m |
| 16 | Sydney Kingsford Smith International Airport (YSSY) | Cape Barren Island Airport (YCBN) | 1 | 1h 4m |
| 17 | Charles de Gaulle International Airport (LFPG) | Fujairah International Airport (OMFJ) | 1 | 6h 25m |
| 18 | Albuquerque International Sunport Airport (KABQ) | Telluride Regional Airport (KTEX) | 1 | 25m |
| 19 | Addison Airport (KADS) | Manassas Regional/Harry P Davis Field (KHEF) | 1 | 2h 14m |
| 20 | Indianapolis International Airport (KIND) | Golden Triangle Regional Airport (KGTR) | 1 | 1h 26m |
| 21 | Julian Hinds Pump Plant Airstrip (73CL) | Henderson Executive Airport (KHND) | 1 | 27m |
| 22 | Chicago Executive Airport (KPWK) | Johnson Memorial Airport (05XS) | 1 | 1h 33m |
| 23 | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 1 | 31m |
| 24 | Bob Hope Airport (KBUR) | Table Rock Airport (OG06) | 1 | 1h 19m |
| 25 | Dallas-Fort Worth International Airport (KDFW) | Denver International Airport (KDEN) | 1 | 1h 33m |
| 26 | Charlotte/Monroe Executive Airport (KEQY) | Brown Field (46NC) | 1 | 15m |
| 27 | Allegheny County Airport (KAGC) | Grant County Airport (KW99) | 1 | 1h 28m |
| 28 | George Bush Intcntl/Houston Airport (KIAH) | Wilson Airport (K4F8) | 1 | 36m |
| 29 | 53TX (53TX) | T-Ranch Airport (XS86) | 1 | 31m |
| 30 | Charles M Schulz/Sonoma County Airport (KSTS) | St George Regional Airport (KSGU) | 1 | 1h 53m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BYF43 | BYF | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-03-28 22:31 UTC | 2026-03-28 23:02 UTC | 31m |
| N6502W |  | Cincinnati Municipal/Lunken Field (KLUK) | Indianapolis Executive Airport (KTYQ) | 2026-03-28 21:53 UTC | 2026-03-28 23:00 UTC | 1h 6m |
| N5107H |  | Green Mountain Airport (WA67) | Scappoose Airport (KSPB) | 2026-03-28 22:34 UTC | 2026-03-28 22:59 UTC | 25m |
| N6090F |  | Addison Airport (KADS) | Jlinn Airport (37TS) | 2026-03-28 21:40 UTC | 2026-03-28 22:52 UTC | 1h 12m |
| N64WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-03-28 22:10 UTC | 2026-03-28 22:50 UTC | 39m |
| N29WB |  | Gnoss Field (KDVO) | CL36 (CL36) | 2026-03-28 21:56 UTC | 2026-03-28 22:48 UTC | 51m |
| CWA922 | CWA | Bow Island Airport (CEF3) | Taber Airport (CED5) | 2026-03-28 22:37 UTC | 2026-03-28 22:48 UTC | 10m |
| EJA830 | EJA | Cuyahoga County Airport (KCGF) | Rocky Mountain Metro Airport (KBJC) | 2026-03-28 19:42 UTC | 2026-03-28 22:43 UTC | 3h 0m |
| THY6429 | Turkish Airlines | Chhatrapati Shivaji International Airport (VABB) | Malpensa International Airport (LIMC) | 2026-03-28 11:12 UTC | 2026-03-28 22:36 UTC | 11h 24m |
| N7718A |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-03-28 21:55 UTC | 2026-03-28 22:33 UTC | 38m |
| HER707 | HER | Laurence G Hanscom Field (KBED) | Laurence G Hanscom Field (KBED) | 2026-03-28 22:29 UTC | 2026-03-28 22:29 UTC | 0m |
| N22VK |  | Chino Airport (KCNO) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-03-28 22:09 UTC | 2026-03-28 22:28 UTC | 18m |
| N620WF |  | Montgomery-Gibbs Executive Airport (KMYF) | Jacqueline Cochran Regional Airport (KTRM) | 2026-03-28 22:02 UTC | 2026-03-28 22:27 UTC | 25m |
| N219PW |  | Charles M Schulz/Sonoma County Airport (KSTS) | St George Regional Airport (KSGU) | 2026-03-28 20:31 UTC | 2026-03-28 22:25 UTC | 1h 53m |
| EFI | EFI | Toowoomba Wellcamp Airport (YBWW) | Ballina Byron Gateway Airport (YBNA) | 2026-03-28 20:58 UTC | 2026-03-28 22:23 UTC | 1h 25m |
| SLG1 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Melfort Airport (CJZ3) | 2026-03-28 22:01 UTC | 2026-03-28 22:23 UTC | 22m |
| ERU22 | ERU | Mc Clellan-Palomar Airport (KCRQ) | Yucca Valley Airport (KL22) | 2026-03-28 21:39 UTC | 2026-03-28 22:23 UTC | 43m |
| QLK20D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-03-28 21:45 UTC | 2026-03-28 22:21 UTC | 35m |
| TGFYL | TGF | La Aurora Airport (MGGT) | La America Airport (MHEI) | 2026-03-28 21:37 UTC | 2026-03-28 22:18 UTC | 40m |
| N734MW |  | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-03-28 21:36 UTC | 2026-03-28 22:17 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
