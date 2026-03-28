# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_19:41:14_UTC-green)

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

**2026-03-28 19:41:14 UTC**

- **10,420** aircraft tracked
- **9,610** currently in the air
- **810** on the ground
- **98** countries
- **100** airports with traffic
- **50** airlines identified
- **213** flight routes (last 2h)
- **1h 12m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | United Airlines | 427 |
| 2 | American Airlines | 425 |
| 3 | Delta Air Lines | 423 |
| 4 | Southwest Airlines | 421 |
| 5 | Ryanair | 336 |
| 6 | SkyWest Airlines | 206 |
| 7 | EJA | 159 |
| 8 | Turkish Airlines | 142 |
| 9 | JetBlue | 133 |
| 10 | Alaska Airlines | 126 |
| 11 | Republic Airways | 105 |
| 12 | Air Canada | 100 |
| 13 | FFT | 80 |
| 14 | WJA | 78 |
| 15 | easyJet | 76 |
| 16 | EJU | 75 |
| 17 | LXJ | 75 |
| 18 | British Airways | 74 |
| 19 | JIA | 70 |
| 20 | ENY | 66 |
| 21 | Scandinavian Airlines | 64 |
| 22 | EDV | 62 |
| 23 | Air France | 58 |
| 24 | AAY | 56 |
| 25 | Vueling | 56 |
| 26 | Lufthansa | 55 |
| 27 | NKS | 53 |
| 28 | CXK | 51 |
| 29 | EXS | 44 |
| 30 | TAP Air Portugal | 42 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 6760 |
| 2 | 🇨🇦 Canada | 453 |
| 3 | 🇬🇧 United Kingdom | 291 |
| 4 | 🇮🇪 Ireland | 263 |
| 5 | 🇹🇷 Turkey | 242 |
| 6 | 🇪🇸 Spain | 165 |
| 7 | 🇩🇪 Germany | 164 |
| 8 | 🏳️ Malta | 157 |
| 9 | 🇲🇽 Mexico | 143 |
| 10 | 🇫🇷 France | 113 |
| 11 | 🇦🇹 Austria | 106 |
| 12 | 🇨🇳 China | 95 |
| 13 | 🇧🇷 Brazil | 94 |
| 14 | 🇵🇱 Poland | 84 |
| 15 | 🇦🇺 Australia | 75 |
| 16 | 🇨🇭 Switzerland | 73 |
| 17 | 🏳️ Republic of Korea | 71 |
| 18 | 🏳️ Kingdom of the Netherlands | 62 |
| 19 | 🇸🇪 Sweden | 58 |
| 20 | 🇮🇳 India | 50 |
| 21 | 🇯🇵 Japan | 48 |
| 22 | 🇵🇹 Portugal | 47 |
| 23 | 🇦🇪 United Arab Emirates | 45 |
| 24 | 🇫🇮 Finland | 40 |
| 25 | 🏳️ Hungary | 39 |
| 26 | 🇨🇱 Chile | 33 |
| 27 | 🇳🇴 Norway | 31 |
| 28 | 🇹🇭 Thailand | 31 |
| 29 | 🏳️ Morocco | 28 |
| 30 | 🏳️ Russian Federation | 28 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 27 |
| 2 | Phoenix Sky Harbor International Airport | Phoenix | US | 25 |
| 3 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 24 |
| 4 | Harry Reid International Airport | Las Vegas | US | 21 |
| 5 | John F Kennedy International Airport | New York | US | 21 |
| 6 | Toronto Pearson International Airport | Mississauga | CA | 20 |
| 7 | General Edward Lawrence Logan International Airport | Boston | US | 19 |
| 8 | Orlando International Airport | Orlando | US | 18 |
| 9 | Calgary International Airport | Calgary | CA | 17 |
| 10 | Chicago O'Hare International Airport | Chicago | US | 16 |
| 11 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 16 |
| 12 | Vancouver International Airport | Richmond | CA | 15 |
| 13 | Washington Dulles International Airport | Washington | US | 15 |
| 14 | Denver International Airport | Denver | US | 14 |
| 15 | Newark Liberty International Airport | Newark | US | 14 |
| 16 | Cancun International Airport | Cancun | MX | 14 |
| 17 | Zurich Airport | Zurich | CH | 13 |
| 18 | El Dorado International Airport | Bogota | CO | 12 |
| 19 | Austin-Bergstrom International Airport | Austin | US | 12 |
| 20 | San Diego International Airport | San Diego | US | 11 |
| 21 | London Gatwick Airport | London | GB | 11 |
| 22 | Los Angeles International Airport | Los Angeles | US | 10 |
| 23 | Melbourne International Airport | Melbourne | AU | 10 |
| 24 | Tampa International Airport | Tampa | US | 9 |
| 25 | Indira Gandhi International Airport | New Delhi | IN | 9 |
| 26 | Witham Field | Stuart | US | 9 |
| 27 | Tokyo International Airport | Tokyo | JP | 9 |
| 28 | Van Nuys Airport | Van Nuys | US | 9 |
| 29 | Salt Lake City International Airport | Salt Lake City | US | 8 |
| 30 | Nashville International Airport | Nashville | US | 8 |
| 31 | Rocky Mountain Metro Airport | Denver | US | 7 |
| 32 | Riverside Airport | Riverside | US | 7 |
| 33 | Chicago Midway International Airport | Chicago | US | 7 |
| 34 | Amsterdam Airport Schiphol | Amsterdam | NL | 7 |
| 35 | Norman Y Mineta San Jose International Airport | San Jose | US | 7 |
| 36 | Laguardia Airport | New York | US | 7 |
| 37 | Auburn University Regional Airport | Auburn | US | 6 |
| 38 | Seattle-Tacoma International Airport | Seattle | US | 6 |
| 39 | Ted Stevens Anchorage International Airport | Anchorage | US | 6 |
| 40 | Chek Lap Kok International Airport | Hong Kong | HK | 6 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 5 | 25m |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 3 | 24m |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2 | 10m |
| 4 | Provo Municipal Airport (KPVU) | K36U (K36U) | 2 | 8m |
| 5 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2 | 40m |
| 6 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2 | 11m |
| 7 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 1 | 21m |
| 8 | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 1 | 11m |
| 9 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 1 | 19m |
| 10 | Del Norte International Airport (MMAN) | General Lucio Blanco International Airport (MMRX) | 1 | 29m |
| 11 | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 1 | 5m |
| 12 | General Ignacio P. Garcia International Airport (MMHO) | Atizapan De Zaragoza Airport (MMJC) | 1 | 2h 7m |
| 13 | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 1 | 0m |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 55m |
| 15 | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 1 | 59m |
| 16 | Alicante International Airport (LEAL) | Leon Airport (LELN) | 1 | 1h 7m |
| 17 | Tenerife Norte Airport (GCXO) | Palma De Mallorca Airport (LEPA) | 1 | 3h 19m |
| 18 | Tenerife Norte Airport (GCXO) | La Morgal Airport (LEMR) | 1 | 2h 30m |
| 19 | London Heathrow Airport (EGLL) | Frankfurt am Main International Airport (EDDF) | 1 | 1h 3m |
| 20 | Cumbernauld Airport (EGPG) | Glasgow International Airport (EGPF) | 1 | 27m |
| 21 | Grenoble-Isere Airport (LFLS) | Bristol International Airport (EGGD) | 1 | 1h 21m |
| 22 | London Luton Airport (EGGW) | Fetesti Air Base (LR80) | 1 | 2h 51m |
| 23 | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 1 | 31m |
| 24 | Manchester Airport (EGCC) | Isparta Airport (LTBM) | 1 | 3h 48m |
| 25 | Manchester Airport (EGCC) | Hoefen Airport (LOIR) | 1 | 1h 39m |
| 26 | London Gatwick Airport (EGKK) | Hoefen Airport (LOIR) | 1 | 1h 22m |
| 27 | Grazzanise Airport (LIRM) | London Gatwick Airport (EGKK) | 1 | 2h 13m |
| 28 | Vienna International Airport (LOWW) | Linate Airport (LIML) | 1 | 1h 7m |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 1 | 22m |
| 30 | Larnaca International Airport (LCLK) | LW72 (LW72) | 1 | 1h 45m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N56966 |  | Mcnary Field (KSLE) | Portland-Hillsboro Airport (KHIO) | 2026-03-28 19:02 UTC | 2026-03-28 19:30 UTC | 27m |
| BRG650 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-03-28 18:57 UTC | 2026-03-28 19:24 UTC | 27m |
| N59073 |  | 8CL0 (8CL0) | Big Bear City Airport (KL35) | 2026-03-28 18:53 UTC | 2026-03-28 19:11 UTC | 18m |
| BRG621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-03-28 18:23 UTC | 2026-03-28 19:10 UTC | 46m |
| N92DV |  | Erie Municipal Airport (KEIK) | Vance Brand Airport (KLMO) | 2026-03-28 16:54 UTC | 2026-03-28 19:09 UTC | 2h 14m |
| N65956 |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-03-28 17:59 UTC | 2026-03-28 19:08 UTC | 1h 8m |
| N121BR |  | Provo Municipal Airport (KPVU) | K36U (K36U) | 2026-03-28 18:54 UTC | 2026-03-28 19:02 UTC | 7m |
| TGCYC | TGC | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-03-28 18:34 UTC | 2026-03-28 19:01 UTC | 26m |
| HK5445 |  | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 2026-03-28 18:48 UTC | 2026-03-28 18:59 UTC | 11m |
| CPA838 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Vancouver International Airport (CYVR) | 2026-03-28 07:51 UTC | 2026-03-28 18:59 UTC | 11h 7m |
| SRG853A | SRG | Cumbernauld Airport (EGPG) | Glasgow International Airport (EGPF) | 2026-03-28 18:26 UTC | 2026-03-28 18:53 UTC | 27m |
| EJM325 | EJM | Naples Municipal Airport (KAPF) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-03-28 16:24 UTC | 2026-03-28 18:53 UTC | 2h 28m |
| N683UF |  | Manchester Boston Regional Airport (KMHT) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-03-28 17:04 UTC | 2026-03-28 18:53 UTC | 1h 49m |
| N511CR |  | Stockton Metro Airport (KSCK) | 8CL9 (8CL9) | 2026-03-28 18:31 UTC | 2026-03-28 18:51 UTC | 20m |
| ACA997 | Air Canada | Licenciado Benito Juarez International Airport (MMMX) | Vancouver International Airport (CYVR) | 2026-03-28 13:41 UTC | 2026-03-28 18:49 UTC | 5h 8m |
| N312FL |  | Indianapolis Executive Airport (KTYQ) | Lakeland Linder International Airport (KLAL) | 2026-03-28 16:42 UTC | 2026-03-28 18:47 UTC | 2h 4m |
| EJA821 | EJA | Norman Y Mineta San Jose International Airport (KSJC) | Bob Hope Airport (KBUR) | 2026-03-28 17:59 UTC | 2026-03-28 18:47 UTC | 47m |
| N570DB |  | Peter O Knight Airport (KTPF) | Peter O Knight Airport (KTPF) | 2026-03-28 17:32 UTC | 2026-03-28 18:45 UTC | 1h 13m |
| N227NH |  | KU77 (KU77) | K36U (K36U) | 2026-03-28 18:32 UTC | 2026-03-28 18:45 UTC | 13m |
| N4512L |  | Sanctuary Ranch Airport (7TS4) | 45TE (45TE) | 2026-03-28 18:40 UTC | 2026-03-28 18:43 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
