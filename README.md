# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_20:01:10_UTC-green)

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

**2026-03-28 20:01:10 UTC**

- **10,456** aircraft tracked
- **9,617** currently in the air
- **839** on the ground
- **98** countries
- **100** airports with traffic
- **50** airlines identified
- **213** flight routes (last 2h)
- **1h 11m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | American Airlines | 458 |
| 2 | United Airlines | 436 |
| 3 | Southwest Airlines | 431 |
| 4 | Delta Air Lines | 424 |
| 5 | Ryanair | 331 |
| 6 | SkyWest Airlines | 221 |
| 7 | EJA | 166 |
| 8 | JetBlue | 131 |
| 9 | Alaska Airlines | 118 |
| 10 | Turkish Airlines | 117 |
| 11 | Republic Airways | 114 |
| 12 | Air Canada | 90 |
| 13 | FFT | 88 |
| 14 | ENY | 84 |
| 15 | easyJet | 80 |
| 16 | EJU | 77 |
| 17 | JIA | 73 |
| 18 | AAY | 71 |
| 19 | LXJ | 71 |
| 20 | British Airways | 71 |
| 21 | WJA | 70 |
| 22 | Scandinavian Airlines | 65 |
| 23 | EDV | 65 |
| 24 | Air France | 58 |
| 25 | Lufthansa | 57 |
| 26 | Vueling | 55 |
| 27 | NKS | 53 |
| 28 | CXK | 49 |
| 29 | TVF | 42 |
| 30 | EWG | 42 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 6744 |
| 2 | 🇨🇦 Canada | 461 |
| 3 | 🇬🇧 United Kingdom | 285 |
| 4 | 🇮🇪 Ireland | 252 |
| 5 | 🇹🇷 Turkey | 209 |
| 6 | 🇩🇪 Germany | 167 |
| 7 | 🇪🇸 Spain | 166 |
| 8 | 🏳️ Malta | 158 |
| 9 | 🇲🇽 Mexico | 135 |
| 10 | 🇫🇷 France | 122 |
| 11 | 🇦🇹 Austria | 107 |
| 12 | 🇨🇳 China | 107 |
| 13 | 🇧🇷 Brazil | 101 |
| 14 | 🇦🇺 Australia | 89 |
| 15 | 🇵🇱 Poland | 79 |
| 16 | 🇨🇭 Switzerland | 77 |
| 17 | 🏳️ Republic of Korea | 74 |
| 18 | 🇸🇪 Sweden | 63 |
| 19 | 🇮🇳 India | 61 |
| 20 | 🇦🇪 United Arab Emirates | 58 |
| 21 | 🏳️ Kingdom of the Netherlands | 57 |
| 22 | 🇵🇹 Portugal | 44 |
| 23 | 🇹🇭 Thailand | 43 |
| 24 | 🇯🇵 Japan | 41 |
| 25 | 🇫🇮 Finland | 40 |
| 26 | 🏳️ Hungary | 36 |
| 27 | 🇳🇴 Norway | 35 |
| 28 | 🇳🇿 New Zealand | 34 |
| 29 | 🇨🇱 Chile | 29 |
| 30 | 🏳️ Greece | 28 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Toronto Pearson International Airport | Mississauga | CA | 32 |
| 2 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 28 |
| 3 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 27 |
| 4 | Harry Reid International Airport | Las Vegas | US | 26 |
| 5 | Phoenix Sky Harbor International Airport | Phoenix | US | 24 |
| 6 | Washington Dulles International Airport | Washington | US | 23 |
| 7 | Calgary International Airport | Calgary | CA | 21 |
| 8 | General Edward Lawrence Logan International Airport | Boston | US | 21 |
| 9 | Los Angeles International Airport | Los Angeles | US | 18 |
| 10 | Orlando International Airport | Orlando | US | 17 |
| 11 | Vancouver International Airport | Richmond | CA | 17 |
| 12 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 17 |
| 13 | Zurich Airport | Zurich | CH | 17 |
| 14 | Cancun International Airport | Cancun | MX | 15 |
| 15 | San Francisco International Airport | San Francisco | US | 15 |
| 16 | San Diego International Airport | San Diego | US | 13 |
| 17 | John F Kennedy International Airport | New York | US | 13 |
| 18 | Chicago O'Hare International Airport | Chicago | US | 13 |
| 19 | Laguardia Airport | New York | US | 12 |
| 20 | Ronald Reagan Washington Ntl Airport | Washington | US | 12 |
| 21 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 11 |
| 22 | Denver International Airport | Denver | US | 11 |
| 23 | London Gatwick Airport | London | GB | 11 |
| 24 | El Dorado International Airport | Bogota | CO | 10 |
| 25 | Sydney Kingsford Smith International Airport | Sydney | AU | 10 |
| 26 | St Louis Lambert International Airport | St Louis | US | 9 |
| 27 | Chek Lap Kok International Airport | Hong Kong | HK | 9 |
| 28 | Salt Lake City International Airport | Salt Lake City | US | 9 |
| 29 | Melbourne International Airport | Melbourne | AU | 9 |
| 30 | Austin-Bergstrom International Airport | Austin | US | 9 |
| 31 | Nashville International Airport | Nashville | US | 8 |
| 32 | Paris-Orly Airport | Paris | FR | 8 |
| 33 | Newark Liberty International Airport | Newark | US | 8 |
| 34 | Chhatrapati Shivaji International Airport | Mumbai | IN | 7 |
| 35 | Norman Y Mineta San Jose International Airport | San Jose | US | 7 |
| 36 | Ted Stevens Anchorage International Airport | Anchorage | US | 6 |
| 37 | Teterboro Airport | Teterboro | US | 6 |
| 38 | Tokyo International Airport | Tokyo | JP | 5 |
| 39 | Rocky Mountain Metro Airport | Denver | US | 5 |
| 40 | Manchester Airport | Manchester | GB | 5 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 4 | 23m |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 3 | 24m |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2 | 10m |
| 4 | Tenerife Norte Airport (GCXO) | La Morgal Airport (LEMR) | 2 | 2h 30m |
| 5 | Provo Municipal Airport (KPVU) | K36U (K36U) | 2 | 8m |
| 6 | Chicago O'Hare International Airport (KORD) | Yonder Airport (NC65) | 2 | 1h 20m |
| 7 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2 | 11m |
| 8 | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 1 | 11m |
| 9 | La Aurora Airport (MGGT) | La America Airport (MHEI) | 1 | 37m |
| 10 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 1 | 19m |
| 11 | Del Norte International Airport (MMAN) | General Lucio Blanco International Airport (MMRX) | 1 | 29m |
| 12 | General Ignacio P. Garcia International Airport (MMHO) | Atizapan De Zaragoza Airport (MMJC) | 1 | 2h 7m |
| 13 | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 1 | 0m |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 55m |
| 15 | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 1 | 59m |
| 16 | Tenerife Norte Airport (GCXO) | Palma De Mallorca Airport (LEPA) | 1 | 3h 19m |
| 17 | Bordeaux-Merignac (BA 106) Airport (LFBD) | Mostaganem Airport (DA14) | 1 | 1h 17m |
| 18 | Faa'a International Airport (NTAA) | Moorea Airport (NTTM) | 1 | 7m |
| 19 | London Heathrow Airport (EGLL) | Frankfurt am Main International Airport (EDDF) | 1 | 1h 3m |
| 20 | Cumbernauld Airport (EGPG) | Glasgow International Airport (EGPF) | 1 | 27m |
| 21 | Grenoble-Isere Airport (LFLS) | Bristol International Airport (EGGD) | 1 | 1h 21m |
| 22 | London Luton Airport (EGGW) | Fetesti Air Base (LR80) | 1 | 2h 51m |
| 23 | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 1 | 31m |
| 24 | London Gatwick Airport (EGKK) | Hoefen Airport (LOIR) | 1 | 1h 22m |
| 25 | Vienna International Airport (LOWW) | Linate Airport (LIML) | 1 | 1h 7m |
| 26 | Helsinki Vantaa Airport (EFHK) | Suomussalmi Airport (EFSU) | 1 | 1h 1m |
| 27 | Helsinki Vantaa Airport (EFHK) | Sodankyla Airport (EFSO) | 1 | 58m |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 1 | 22m |
| 29 | Larnaca International Airport (LCLK) | LW72 (LW72) | 1 | 1h 45m |
| 30 | Ørland Airport (ENOL) | Trondheim Airport Vaernes (ENVA) | 1 | 18m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-03-28 16:43 UTC | 2026-03-28 19:42 UTC | 2h 58m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-03-28 19:21 UTC | 2026-03-28 19:41 UTC | 19m |
| N9957M |  | Homer Airport (PAHO) | Seldovia Airport (PASO) | 2026-03-28 19:26 UTC | 2026-03-28 19:36 UTC | 10m |
| N758NL |  | San Bernardino International Airport (KSBD) | Riverside Airport (KRAL) | 2026-03-28 19:21 UTC | 2026-03-28 19:32 UTC | 10m |
| N56966 |  | Mcnary Field (KSLE) | Portland-Hillsboro Airport (KHIO) | 2026-03-28 19:02 UTC | 2026-03-28 19:30 UTC | 27m |
| N25XP |  | Dallas Love Field (KDAL) | Austin-Bergstrom International Airport (KAUS) | 2026-03-28 18:47 UTC | 2026-03-28 19:26 UTC | 38m |
| N682AC |  | TE77 (TE77) | TE77 (TE77) | 2026-03-28 19:08 UTC | 2026-03-28 19:25 UTC | 17m |
| SCU42 | SCU | Double W Airport (3OK7) | Double W Airport (3OK7) | 2026-03-28 19:21 UTC | 2026-03-28 19:25 UTC | 3m |
| BRG650 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-03-28 18:57 UTC | 2026-03-28 19:24 UTC | 27m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-03-28 18:59 UTC | 2026-03-28 19:24 UTC | 24m |
| N635KC |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-03-28 18:35 UTC | 2026-03-28 19:20 UTC | 44m |
| EAI48D | EAI | Dublin Airport (EIDW) | Letterkenny Airport (EILT) | 2026-03-28 18:46 UTC | 2026-03-28 19:15 UTC | 28m |
| N59073 |  | 8CL0 (8CL0) | Big Bear City Airport (KL35) | 2026-03-28 18:53 UTC | 2026-03-28 19:11 UTC | 18m |
| BRG621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-03-28 18:23 UTC | 2026-03-28 19:10 UTC | 46m |
| LYM3583 | LYM | Denver International Airport (KDEN) | Leach Airport (K1V8) | 2026-03-28 18:48 UTC | 2026-03-28 19:10 UTC | 21m |
| N92DV |  | Erie Municipal Airport (KEIK) | Vance Brand Airport (KLMO) | 2026-03-28 16:54 UTC | 2026-03-28 19:09 UTC | 2h 14m |
| N65956 |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-03-28 17:59 UTC | 2026-03-28 19:08 UTC | 1h 8m |
|  |  | G Bar F Ranch Airport (NM84) | G Bar F Ranch Airport (NM84) | 2026-03-28 19:07 UTC | 2026-03-28 19:07 UTC | 0m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-03-28 18:39 UTC | 2026-03-28 19:06 UTC | 26m |
| N8515P |  | KU42 (KU42) | Brigham City Regional Airport (KBMC) | 2026-03-28 18:42 UTC | 2026-03-28 19:05 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
