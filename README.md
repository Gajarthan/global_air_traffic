# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_17:59:26_UTC-green)

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

**2026-03-28 17:59:26 UTC**

- **11,161** aircraft tracked
- **10,297** currently in the air
- **864** on the ground
- **102** countries
- **100** airports with traffic
- **50** airlines identified
- **187** flight routes (last 2h)
- **1h 13m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | American Airlines | 467 |
| 2 | Southwest Airlines | 451 |
| 3 | Delta Air Lines | 446 |
| 4 | United Airlines | 444 |
| 5 | Ryanair | 361 |
| 6 | SkyWest Airlines | 217 |
| 7 | EJA | 169 |
| 8 | Alaska Airlines | 126 |
| 9 | JetBlue | 117 |
| 10 | Turkish Airlines | 108 |
| 11 | Republic Airways | 107 |
| 12 | easyJet | 103 |
| 13 | Lufthansa | 100 |
| 14 | Air Canada | 99 |
| 15 | ENY | 98 |
| 16 | FFT | 95 |
| 17 | KLM Royal Dutch | 82 |
| 18 | Scandinavian Airlines | 79 |
| 19 | LXJ | 73 |
| 20 | Air France | 73 |
| 21 | EXS | 69 |
| 22 | AAY | 64 |
| 23 | IndiGo | 62 |
| 24 | WJA | 62 |
| 25 | JIA | 62 |
| 26 | EJU | 61 |
| 27 | Vueling | 60 |
| 28 | CXK | 58 |
| 29 | British Airways | 58 |
| 30 | NKS | 57 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 7183 |
| 2 | 🇨🇦 Canada | 455 |
| 3 | 🇬🇧 United Kingdom | 356 |
| 4 | 🇮🇪 Ireland | 274 |
| 5 | 🇩🇪 Germany | 226 |
| 6 | 🇹🇷 Turkey | 204 |
| 7 | 🏳️ Malta | 172 |
| 8 | 🇪🇸 Spain | 157 |
| 9 | 🇫🇷 France | 143 |
| 10 | 🇮🇳 India | 142 |
| 11 | 🇲🇽 Mexico | 129 |
| 12 | 🇨🇳 China | 129 |
| 13 | 🇧🇷 Brazil | 108 |
| 14 | 🏳️ Kingdom of the Netherlands | 106 |
| 15 | 🇵🇱 Poland | 102 |
| 16 | 🇦🇹 Austria | 99 |
| 17 | 🇸🇪 Sweden | 75 |
| 18 | 🇨🇭 Switzerland | 65 |
| 19 | 🇵🇹 Portugal | 52 |
| 20 | 🏳️ Hungary | 48 |
| 21 | 🏳️ Republic of Korea | 41 |
| 22 | 🇪🇬 Egypt | 40 |
| 23 | 🇦🇪 United Arab Emirates | 39 |
| 24 | 🏳️ Russian Federation | 39 |
| 25 | 🇯🇵 Japan | 36 |
| 26 | 🇹🇼 Taiwan | 35 |
| 27 | 🇧🇪 Belgium | 33 |
| 28 | 🇫🇮 Finland | 33 |
| 29 | 🇨🇱 Chile | 30 |
| 30 | 🇳🇴 Norway | 30 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 27 |
| 2 | Phoenix Sky Harbor International Airport | Phoenix | US | 26 |
| 3 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 25 |
| 4 | Toronto Pearson International Airport | Mississauga | CA | 25 |
| 5 | Harry Reid International Airport | Las Vegas | US | 23 |
| 6 | General Edward Lawrence Logan International Airport | Boston | US | 19 |
| 7 | Denver International Airport | Denver | US | 18 |
| 8 | Chicago O'Hare International Airport | Chicago | US | 15 |
| 9 | Cancun International Airport | Cancun | MX | 15 |
| 10 | Orlando International Airport | Orlando | US | 15 |
| 11 | Calgary International Airport | Calgary | CA | 15 |
| 12 | San Diego International Airport | San Diego | US | 14 |
| 13 | Zurich Airport | Zurich | CH | 14 |
| 14 | Los Angeles International Airport | Los Angeles | US | 13 |
| 15 | Vancouver International Airport | Richmond | CA | 13 |
| 16 | Austin-Bergstrom International Airport | Austin | US | 12 |
| 17 | San Francisco International Airport | San Francisco | US | 12 |
| 18 | Amsterdam Airport Schiphol | Amsterdam | NL | 12 |
| 19 | Indira Gandhi International Airport | New Delhi | IN | 11 |
| 20 | Newark Liberty International Airport | Newark | US | 11 |
| 21 | El Dorado International Airport | Bogota | CO | 10 |
| 22 | Chhatrapati Shivaji International Airport | Mumbai | IN | 10 |
| 23 | Rocky Mountain Metro Airport | Denver | US | 10 |
| 24 | Laguardia Airport | New York | US | 10 |
| 25 | London Gatwick Airport | London | GB | 10 |
| 26 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 10 |
| 27 | Southwest Florida International Airport | Fort Myers | US | 9 |
| 28 | Chek Lap Kok International Airport | Hong Kong | HK | 9 |
| 29 | Chicago Midway International Airport | Chicago | US | 9 |
| 30 | North Las Vegas Airport | Las Vegas | US | 9 |
| 31 | John F Kennedy International Airport | New York | US | 9 |
| 32 | Washington Dulles International Airport | Washington | US | 8 |
| 33 | Scottsdale Airport | Scottsdale | US | 8 |
| 34 | Tampa International Airport | Tampa | US | 8 |
| 35 | Stuttgart Airport | Stuttgart | DE | 7 |
| 36 | Madrid Barajas International Airport | Madrid | ES | 7 |
| 37 | Nashville International Airport | Nashville | US | 7 |
| 38 | Portland International Airport | Portland | US | 7 |
| 39 | Ronald Reagan Washington Ntl Airport | Washington | US | 7 |
| 40 | Paris-Orly Airport | Paris | FR | 7 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 4 | 24m |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 3 | 28m |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2 | 22m |
| 4 | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 2 | 32m |
| 5 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2 | 27m |
| 6 | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2 | 12h 50m |
| 7 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2 | 14m |
| 8 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 2 | 54m |
| 9 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2 | 24m |
| 10 | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2 | 12m |
| 11 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2 | 12m |
| 12 | Lanseria Airport (FALA) | Newcastle Airport (FANC) | 1 | 23m |
| 13 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 1 | 10m |
| 14 | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 1 | 26m |
| 15 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 1 | 10m |
| 16 | General Abelardo L. Rodriguez International Airport (MMTJ) | Atizapan De Zaragoza Airport (MMJC) | 1 | 2h 54m |
| 17 | Rocky Mountain Metro Airport (KBJC) | CO86 (CO86) | 1 | 12m |
| 18 | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 1 | 19m |
| 19 | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 1 | 55m |
| 20 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 1 | 7m |
| 21 | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 1 | 1h 14m |
| 22 | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 1 | 1h 59m |
| 23 | Frankfurt am Main International Airport (EDDF) | Santorini Airport (LGSR) | 1 | 2h 26m |
| 24 | Frankfurt am Main International Airport (EDDF) | Langhennersdorf Airport (EDOH) | 1 | 41m |
| 25 | London Gatwick Airport (EGKK) | Hoefen Airport (LOIR) | 1 | 1h 24m |
| 26 | Oslo Gardermoen Airport (ENGM) | Macau International Airport (VMMC) | 1 | 18h 53m |
| 27 | Amsterdam Airport Schiphol (EHAM) | Malpensa International Airport (LIMC) | 1 | 1h 27m |
| 28 | Warsaw Chopin Airport (EPWA) | Sondrio Caiolo Airport (LILO) | 1 | 1h 30m |
| 29 | Amsterdam Airport Schiphol (EHAM) | Hoefen Airport (LOIR) | 1 | 1h 3m |
| 30 | Amsterdam Airport Schiphol (EHAM) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 1 | 1h 44m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASA495 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Bermuda Dunes Airport (KUDD) | 2026-03-28 15:24 UTC | 2026-03-28 17:35 UTC | 2h 10m |
| N1011N |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-03-28 16:57 UTC | 2026-03-28 17:30 UTC | 32m |
| CGMPE | CGM | Edmonton International Airport (CYEG) | Calgary / Springbank Airport (CYBW) | 2026-03-28 16:39 UTC | 2026-03-28 17:26 UTC | 46m |
| N75SM |  | 1CO7 (1CO7) | Salida/Harriett Alexander Field (KANK) | 2026-03-28 17:03 UTC | 2026-03-28 17:25 UTC | 21m |
| N64PW |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-03-28 16:57 UTC | 2026-03-28 17:25 UTC | 27m |
| PTOGE | PTO | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-03-28 17:07 UTC | 2026-03-28 17:21 UTC | 13m |
| TGRWC | TGR | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-03-28 16:56 UTC | 2026-03-28 17:18 UTC | 22m |
| N609SA |  | Fort Worth Meacham International Airport (KFTW) | Eagle Airport (TA51) | 2026-03-28 16:39 UTC | 2026-03-28 17:17 UTC | 37m |
| N611TX |  | Easley Acres Airport (33NC) | WV11 (WV11) | 2026-03-28 16:36 UTC | 2026-03-28 17:16 UTC | 40m |
| N107UV |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-03-28 17:07 UTC | 2026-03-28 17:16 UTC | 8m |
| N45VU |  | Eagle Creek Airpark (KEYE) | Indianapolis Executive Airport (KTYQ) | 2026-03-28 16:57 UTC | 2026-03-28 17:14 UTC | 16m |
| TGCSC | TGC | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 2026-03-28 16:47 UTC | 2026-03-28 17:14 UTC | 26m |
| CAP2029 | CAP | Houk Field (28OH) | Houk Field (28OH) | 2026-03-28 16:14 UTC | 2026-03-28 17:10 UTC | 56m |
| ERU79 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Rimrock Airport (48AZ) | 2026-03-28 16:50 UTC | 2026-03-28 17:09 UTC | 19m |
| N5253X |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-03-28 16:51 UTC | 2026-03-28 17:08 UTC | 16m |
| PHX303 | PHX | Halifax Robert L. Stanfield International Airport (CYHZ) | Toronto Pearson International Airport (CYYZ) | 2026-03-28 15:02 UTC | 2026-03-28 17:08 UTC | 2h 5m |
| DLH8NL | Lufthansa | Frankfurt am Main International Airport (EDDF) | Langhennersdorf Airport (EDOH) | 2026-03-28 16:26 UTC | 2026-03-28 17:08 UTC | 41m |
| BRCAT04 | BRC | 2 X 4 Ranch Airport (NM47) | 2 X 4 Ranch Airport (NM47) | 2026-03-28 16:38 UTC | 2026-03-28 17:05 UTC | 26m |
| N827EV |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-03-28 17:02 UTC | 2026-03-28 17:03 UTC | 1m |
| N527MT |  | Brewton Municipal Airport (K12J) | Pensacola International Airport (KPNS) | 2026-03-28 16:40 UTC | 2026-03-28 17:01 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
