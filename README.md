# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_19:03:12_UTC-green)

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

**2026-03-28 19:03:12 UTC**

- **10,747** aircraft tracked
- **9,923** currently in the air
- **824** on the ground
- **103** countries
- **100** airports with traffic
- **50** airlines identified
- **218** flight routes (last 2h)
- **1h 12m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Southwest Airlines | 433 |
| 2 | American Airlines | 422 |
| 3 | Delta Air Lines | 414 |
| 4 | United Airlines | 412 |
| 5 | Ryanair | 319 |
| 6 | SkyWest Airlines | 198 |
| 7 | EJA | 157 |
| 8 | Turkish Airlines | 134 |
| 9 | Alaska Airlines | 127 |
| 10 | JetBlue | 121 |
| 11 | Republic Airways | 116 |
| 12 | Air Canada | 96 |
| 13 | LXJ | 90 |
| 14 | FFT | 84 |
| 15 | easyJet | 79 |
| 16 | British Airways | 75 |
| 17 | EJU | 72 |
| 18 | ENY | 72 |
| 19 | Lufthansa | 70 |
| 20 | EDV | 68 |
| 21 | WJA | 67 |
| 22 | Scandinavian Airlines | 66 |
| 23 | AAY | 59 |
| 24 | JIA | 59 |
| 25 | CXK | 57 |
| 26 | Vueling | 55 |
| 27 | NKS | 52 |
| 28 | Air France | 50 |
| 29 | EXS | 49 |
| 30 | IndiGo | 42 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 7000 |
| 2 | 🇨🇦 Canada | 442 |
| 3 | 🇬🇧 United Kingdom | 304 |
| 4 | 🇮🇪 Ireland | 266 |
| 5 | 🇹🇷 Turkey | 236 |
| 6 | 🇩🇪 Germany | 190 |
| 7 | 🏳️ Malta | 151 |
| 8 | 🇪🇸 Spain | 148 |
| 9 | 🇲🇽 Mexico | 130 |
| 10 | 🇧🇷 Brazil | 112 |
| 11 | 🇫🇷 France | 110 |
| 12 | 🇨🇳 China | 107 |
| 13 | 🇦🇹 Austria | 96 |
| 14 | 🇮🇳 India | 91 |
| 15 | 🇵🇱 Poland | 81 |
| 16 | 🏳️ Republic of Korea | 67 |
| 17 | 🇨🇭 Switzerland | 65 |
| 18 | 🇸🇪 Sweden | 64 |
| 19 | 🏳️ Kingdom of the Netherlands | 62 |
| 20 | 🇯🇵 Japan | 48 |
| 21 | 🇵🇹 Portugal | 47 |
| 22 | 🏳️ Hungary | 45 |
| 23 | 🇦🇺 Australia | 44 |
| 24 | 🇫🇮 Finland | 44 |
| 25 | 🇦🇪 United Arab Emirates | 43 |
| 26 | 🇨🇱 Chile | 41 |
| 27 | 🏳️ Morocco | 39 |
| 28 | 🇳🇴 Norway | 37 |
| 29 | 🇸🇬 Singapore | 33 |
| 30 | 🇹🇼 Taiwan | 30 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Toronto Pearson International Airport | Mississauga | CA | 28 |
| 2 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 26 |
| 3 | Harry Reid International Airport | Las Vegas | US | 23 |
| 4 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 21 |
| 5 | Calgary International Airport | Calgary | CA | 21 |
| 6 | Chicago O'Hare International Airport | Chicago | US | 20 |
| 7 | Zurich Airport | Zurich | CH | 20 |
| 8 | Austin-Bergstrom International Airport | Austin | US | 19 |
| 9 | Phoenix Sky Harbor International Airport | Phoenix | US | 18 |
| 10 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 17 |
| 11 | Amsterdam Airport Schiphol | Amsterdam | NL | 17 |
| 12 | Sydney Kingsford Smith International Airport | Sydney | AU | 16 |
| 13 | Vancouver International Airport | Richmond | CA | 15 |
| 14 | Laguardia Airport | New York | US | 15 |
| 15 | Los Angeles International Airport | Los Angeles | US | 14 |
| 16 | John F Kennedy International Airport | New York | US | 13 |
| 17 | Orlando International Airport | Orlando | US | 12 |
| 18 | San Diego International Airport | San Diego | US | 12 |
| 19 | El Dorado International Airport | Bogota | CO | 11 |
| 20 | Cancun International Airport | Cancun | MX | 11 |
| 21 | Newark Liberty International Airport | Newark | US | 11 |
| 22 | Paris-Orly Airport | Paris | FR | 11 |
| 23 | General Edward Lawrence Logan International Airport | Boston | US | 11 |
| 24 | San Francisco International Airport | San Francisco | US | 9 |
| 25 | Washington Dulles International Airport | Washington | US | 9 |
| 26 | Nashville International Airport | Nashville | US | 8 |
| 27 | London Gatwick Airport | London | GB | 8 |
| 28 | Melbourne International Airport | Melbourne | AU | 8 |
| 29 | Indira Gandhi International Airport | New Delhi | IN | 7 |
| 30 | Rocky Mountain Metro Airport | Denver | US | 7 |
| 31 | North Las Vegas Airport | Las Vegas | US | 7 |
| 32 | Jorge Newbery Airpark | Buenos Aires | AR | 6 |
| 33 | Van Nuys Airport | Van Nuys | US | 6 |
| 34 | Cologne Bonn Airport | Cologne | DE | 6 |
| 35 | Riverside Airport | Riverside | US | 6 |
| 36 | Witham Field | Stuart | US | 6 |
| 37 | Tampa International Airport | Tampa | US | 6 |
| 38 | Southwest Florida International Airport | Fort Myers | US | 6 |
| 39 | Logan-Cache Airport | Logan | US | 5 |
| 40 | La Aurora Airport | Guatemala City | GT | 5 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 4 | 24m |
| 2 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 4 | 23m |
| 3 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 3 | 19m |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2 | 10m |
| 5 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2 | 14m |
| 6 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2 | 27m |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 2 | 14m |
| 8 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 2 | 1h 47m |
| 9 | Alicante International Airport (LEAL) | Mostaganem Airport (DA14) | 1 | 25m |
| 10 | El Dorado International Airport (SKBO) | Santiago Vila Airport (SKGI) | 1 | 11m |
| 11 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1 | 26m |
| 12 | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 1 | 26m |
| 13 | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 1 | 47m |
| 14 | Del Norte International Airport (MMAN) | General Lucio Blanco International Airport (MMRX) | 1 | 29m |
| 15 | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 1 | 10m |
| 16 | General Mariano Escobedo International Airport (MMMY) | Agualeguas Old Airport (MM44) | 1 | 34m |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 54m |
| 18 | London Heathrow Airport (EGLL) | Vitoria/Foronda Airport (LEVT) | 1 | 1h 8m |
| 19 | Alicante International Airport (LEAL) | Leon Airport (LELN) | 1 | 1h 7m |
| 20 | Malaga Airport (LEMG) | La Morgal Airport (LEMR) | 1 | 1h 11m |
| 21 | Tenerife Norte Airport (GCXO) | Vitoria/Foronda Airport (LEVT) | 1 | 2h 32m |
| 22 | Charles de Gaulle International Airport (LFPG) | Rabat-Sale Airport (GMME) | 1 | 2h 20m |
| 23 | Paris-Orly Airport (LFPO) | Saida Airport (DA15) | 1 | 1h 58m |
| 24 | Dusseldorf International Airport (EDDL) | Grobnicko Polje Airport (LDRG) | 1 | 1h 22m |
| 25 | Frankfurt am Main International Airport (EDDF) | Langhennersdorf Airport (EDOH) | 1 | 41m |
| 26 | Frankfurt am Main International Airport (EDDF) | Capua Airport (LIAU) | 1 | 1h 20m |
| 27 | Munich International Airport (EDDM) | Kalamata Airport (LGKL) | 1 | 1h 51m |
| 28 | London Heathrow Airport (EGLL) | Hamburg Airport (EDDH) | 1 | 1h 6m |
| 29 | London Stansted Airport (EGSS) | Visoko Sport Airfield (LQVI) | 1 | 1h 54m |
| 30 | Oslo Gardermoen Airport (ENGM) | Macau International Airport (VMMC) | 1 | 18h 53m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ACA997 | Air Canada | Licenciado Benito Juarez International Airport (MMMX) | Vancouver International Airport (CYVR) | 2026-03-28 13:41 UTC | 2026-03-28 18:49 UTC | 5h 8m |
| N570DB |  | Peter O Knight Airport (KTPF) | Peter O Knight Airport (KTPF) | 2026-03-28 17:32 UTC | 2026-03-28 18:45 UTC | 1h 13m |
| N758NL |  | Ramona Airport (KRNM) | Hemet-Ryan Airport (KHMT) | 2026-03-28 18:11 UTC | 2026-03-28 18:40 UTC | 28m |
| BRCAT05 | BRC | Roswell Air Center Airport (KROW) | G Bar F Ranch Airport (NM84) | 2026-03-28 18:28 UTC | 2026-03-28 18:39 UTC | 11m |
| N120FM |  | Rocky Mountain Metro Airport (KBJC) | Northern Colorado Regional Airport (KFNL) | 2026-03-28 17:38 UTC | 2026-03-28 18:38 UTC | 1h 0m |
| NHZ25 | NHZ | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-03-28 18:01 UTC | 2026-03-28 18:32 UTC | 31m |
| N9577M |  | Bermuda Dunes Airport (KUDD) | Bermuda Dunes Airport (KUDD) | 2026-03-28 18:31 UTC | 2026-03-28 18:32 UTC | 0m |
| N9182J |  | Newport Sky Park Airport (ME68) | Bangor International Airport (KBGR) | 2026-03-28 17:53 UTC | 2026-03-28 18:29 UTC | 35m |
| EJA272 | EJA | Harry Reid International Airport (KLAS) | Rocky Mountain Metro Airport (KBJC) | 2026-03-28 17:10 UTC | 2026-03-28 18:26 UTC | 1h 15m |
| N226LL |  | 16PA (16PA) | Allegheny County Airport (KAGC) | 2026-03-28 17:59 UTC | 2026-03-28 18:23 UTC | 24m |
| DOC | DOC | Ørland Airport (ENOL) | Trondheim Airport Vaernes (ENVA) | 2026-03-28 18:04 UTC | 2026-03-28 18:22 UTC | 18m |
| N6601K |  | Usaf Academy Davis Airfield (KAFF) | Limon Municipal Airport (KLIC) | 2026-03-28 17:53 UTC | 2026-03-28 18:22 UTC | 29m |
| TGKBG | TGK | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-03-28 18:00 UTC | 2026-03-28 18:22 UTC | 21m |
| N403JS |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-03-28 12:59 UTC | 2026-03-28 18:22 UTC | 5h 22m |
| N574SA |  | Hayward Executive Airport (KHWD) | Tracy Municipal Airport (KTCY) | 2026-03-28 17:51 UTC | 2026-03-28 18:19 UTC | 28m |
| N429CF |  | Dallas Executive Airport (KRBD) | Baum Airport (TA46) | 2026-03-28 17:54 UTC | 2026-03-28 18:16 UTC | 21m |
| N365KS |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-03-28 17:48 UTC | 2026-03-28 18:16 UTC | 27m |
| N6796H |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Christensen Ranch Airport (9CL2) | 2026-03-28 17:51 UTC | 2026-03-28 18:16 UTC | 25m |
| BRCAT16 | BRC | Jenkins Airport (NM87) | Roswell Air Center Airport (KROW) | 2026-03-28 17:34 UTC | 2026-03-28 18:15 UTC | 40m |
| TGJFC | TGJ | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-03-28 18:07 UTC | 2026-03-28 18:12 UTC | 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
