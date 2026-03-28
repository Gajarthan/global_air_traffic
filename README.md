# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_18:56:03_UTC-green)

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

**2026-03-28 18:56:03 UTC**

- **10,859** aircraft tracked
- **10,014** currently in the air
- **845** on the ground
- **100** countries
- **100** airports with traffic
- **50** airlines identified
- **218** flight routes (last 2h)
- **1h 11m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Southwest Airlines | 432 |
| 2 | American Airlines | 431 |
| 3 | United Airlines | 425 |
| 4 | Delta Air Lines | 424 |
| 5 | Ryanair | 326 |
| 6 | SkyWest Airlines | 204 |
| 7 | EJA | 159 |
| 8 | Turkish Airlines | 131 |
| 9 | Alaska Airlines | 127 |
| 10 | JetBlue | 117 |
| 11 | Republic Airways | 112 |
| 12 | LXJ | 91 |
| 13 | Air Canada | 90 |
| 14 | easyJet | 87 |
| 15 | FFT | 86 |
| 16 | Lufthansa | 79 |
| 17 | British Airways | 74 |
| 18 | ENY | 73 |
| 19 | WJA | 69 |
| 20 | EJU | 68 |
| 21 | Scandinavian Airlines | 67 |
| 22 | EDV | 64 |
| 23 | JIA | 62 |
| 24 | CXK | 61 |
| 25 | AAY | 61 |
| 26 | Vueling | 56 |
| 27 | Air France | 56 |
| 28 | NKS | 51 |
| 29 | EXS | 51 |
| 30 | LATAM Airlines | 49 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 7083 |
| 2 | 🇨🇦 Canada | 434 |
| 3 | 🇬🇧 United Kingdom | 320 |
| 4 | 🇮🇪 Ireland | 271 |
| 5 | 🇹🇷 Turkey | 233 |
| 6 | 🇩🇪 Germany | 201 |
| 7 | 🏳️ Malta | 151 |
| 8 | 🇪🇸 Spain | 146 |
| 9 | 🇧🇷 Brazil | 132 |
| 10 | 🇲🇽 Mexico | 130 |
| 11 | 🇫🇷 France | 116 |
| 12 | 🇨🇳 China | 97 |
| 13 | 🇮🇳 India | 93 |
| 14 | 🇦🇹 Austria | 92 |
| 15 | 🇵🇱 Poland | 81 |
| 16 | 🇸🇪 Sweden | 67 |
| 17 | 🇨🇭 Switzerland | 66 |
| 18 | 🏳️ Kingdom of the Netherlands | 62 |
| 19 | 🏳️ Republic of Korea | 55 |
| 20 | 🇵🇹 Portugal | 49 |
| 21 | 🇯🇵 Japan | 48 |
| 22 | 🇫🇮 Finland | 44 |
| 23 | 🏳️ Hungary | 43 |
| 24 | 🇨🇱 Chile | 41 |
| 25 | 🇦🇪 United Arab Emirates | 41 |
| 26 | 🏳️ Morocco | 37 |
| 27 | 🇦🇺 Australia | 32 |
| 28 | 🇸🇬 Singapore | 32 |
| 29 | 🇳🇴 Norway | 31 |
| 30 | 🇹🇼 Taiwan | 31 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 30 |
| 2 | Toronto Pearson International Airport | Mississauga | CA | 28 |
| 3 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 23 |
| 4 | Harry Reid International Airport | Las Vegas | US | 23 |
| 5 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 22 |
| 6 | Phoenix Sky Harbor International Airport | Phoenix | US | 20 |
| 7 | Calgary International Airport | Calgary | CA | 20 |
| 8 | Los Angeles International Airport | Los Angeles | US | 18 |
| 9 | Zurich Airport | Zurich | CH | 18 |
| 10 | Amsterdam Airport Schiphol | Amsterdam | NL | 17 |
| 11 | Austin-Bergstrom International Airport | Austin | US | 14 |
| 12 | Vancouver International Airport | Richmond | CA | 14 |
| 13 | San Diego International Airport | San Diego | US | 14 |
| 14 | Chicago O'Hare International Airport | Chicago | US | 14 |
| 15 | Rocky Mountain Metro Airport | Denver | US | 14 |
| 16 | Cancun International Airport | Cancun | MX | 13 |
| 17 | Newark Liberty International Airport | Newark | US | 13 |
| 18 | London Gatwick Airport | London | GB | 12 |
| 19 | Nashville International Airport | Nashville | US | 11 |
| 20 | El Dorado International Airport | Bogota | CO | 11 |
| 21 | General Edward Lawrence Logan International Airport | Boston | US | 11 |
| 22 | Orlando International Airport | Orlando | US | 10 |
| 23 | Ronald Reagan Washington Ntl Airport | Washington | US | 10 |
| 24 | Van Nuys Airport | Van Nuys | US | 9 |
| 25 | John F Kennedy International Airport | New York | US | 9 |
| 26 | Manchester Airport | Manchester | GB | 9 |
| 27 | Tampa International Airport | Tampa | US | 8 |
| 28 | Laguardia Airport | New York | US | 8 |
| 29 | Paris-Orly Airport | Paris | FR | 8 |
| 30 | Washington Dulles International Airport | Washington | US | 8 |
| 31 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 8 |
| 32 | La Aurora Airport | Guatemala City | GT | 7 |
| 33 | Witham Field | Stuart | US | 7 |
| 34 | Sydney Kingsford Smith International Airport | Sydney | AU | 7 |
| 35 | Salt Lake City International Airport | Salt Lake City | US | 7 |
| 36 | Southwest Florida International Airport | Fort Myers | US | 7 |
| 37 | Denver International Airport | Denver | US | 7 |
| 38 | Indira Gandhi International Airport | New Delhi | IN | 6 |
| 39 | Riverside Airport | Riverside | US | 6 |
| 40 | Malpensa International Airport | Milan | IT | 6 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 4 | 24m |
| 2 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 4 | 23m |
| 3 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 3 | 19m |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2 | 28m |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2 | 10m |
| 6 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2 | 14m |
| 7 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2 | 27m |
| 8 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 2 | 1h 47m |
| 9 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2 | 12m |
| 10 | Alicante International Airport (LEAL) | Mostaganem Airport (DA14) | 1 | 25m |
| 11 | El Dorado International Airport (SKBO) | Santiago Vila Airport (SKGI) | 1 | 11m |
| 12 | El Dorado International Airport (SKBO) | Vanguardia Airport (SKVV) | 1 | 16m |
| 13 | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 1 | 26m |
| 14 | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 1 | 47m |
| 15 | General Mariano Escobedo International Airport (MMMY) | Agualeguas Old Airport (MM44) | 1 | 34m |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 54m |
| 17 | London Heathrow Airport (EGLL) | Vitoria/Foronda Airport (LEVT) | 1 | 1h 8m |
| 18 | Alicante International Airport (LEAL) | Leon Airport (LELN) | 1 | 1h 7m |
| 19 | Valencia Airport (LEVC) | Vitoria/Foronda Airport (LEVT) | 1 | 48m |
| 20 | Malaga Airport (LEMG) | La Morgal Airport (LEMR) | 1 | 1h 11m |
| 21 | Tenerife Norte Airport (GCXO) | Vitoria/Foronda Airport (LEVT) | 1 | 2h 32m |
| 22 | Charles de Gaulle International Airport (LFPG) | Mostaganem Airport (DA14) | 1 | 1h 54m |
| 23 | Paris-Orly Airport (LFPO) | Saida Airport (DA15) | 1 | 1h 58m |
| 24 | Paris-Orly Airport (LFPO) | Ifrane Airport (GMFI) | 1 | 2h 16m |
| 25 | Stuttgart Airport (EDDS) | Lanzarote Airport (GCRR) | 1 | 3h 49m |
| 26 | Dusseldorf International Airport (EDDL) | Grobnicko Polje Airport (LDRG) | 1 | 1h 22m |
| 27 | Frankfurt am Main International Airport (EDDF) | Langhennersdorf Airport (EDOH) | 1 | 41m |
| 28 | Frankfurt am Main International Airport (EDDF) | Capua Airport (LIAU) | 1 | 1h 20m |
| 29 | Munich International Airport (EDDM) | Kalamata Airport (LGKL) | 1 | 1h 51m |
| 30 | London Heathrow Airport (EGLL) | Hamburg Airport (EDDH) | 1 | 1h 6m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N758NL |  | Ramona Airport (KRNM) | Hemet-Ryan Airport (KHMT) | 2026-03-28 18:11 UTC | 2026-03-28 18:40 UTC | 28m |
| BRCAT05 | BRC | Roswell Air Center Airport (KROW) | G Bar F Ranch Airport (NM84) | 2026-03-28 18:28 UTC | 2026-03-28 18:39 UTC | 11m |
| N120FM |  | Rocky Mountain Metro Airport (KBJC) | Northern Colorado Regional Airport (KFNL) | 2026-03-28 17:38 UTC | 2026-03-28 18:38 UTC | 1h 0m |
| NHZ25 | NHZ | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-03-28 18:01 UTC | 2026-03-28 18:32 UTC | 31m |
| N9182J |  | Newport Sky Park Airport (ME68) | Bangor International Airport (KBGR) | 2026-03-28 17:53 UTC | 2026-03-28 18:29 UTC | 35m |
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
| N73910 |  | Mckinney Ntl Airport (KTKI) | Commerce Municipal Airport (K2F7) | 2026-03-28 17:40 UTC | 2026-03-28 18:07 UTC | 26m |
| N121BR |  | Provo Municipal Airport (KPVU) | K36U (K36U) | 2026-03-28 17:58 UTC | 2026-03-28 18:06 UTC | 8m |
| N314LM |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-03-28 17:43 UTC | 2026-03-28 18:05 UTC | 21m |
| N561ND |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-03-28 17:30 UTC | 2026-03-28 18:05 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
