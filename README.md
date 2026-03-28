# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_18:29:20_UTC-green)

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

**2026-03-28 18:29:20 UTC**

- **10,893** aircraft tracked
- **10,079** currently in the air
- **814** on the ground
- **98** countries
- **100** airports with traffic
- **50** airlines identified
- **213** flight routes (last 2h)
- **1h 7m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Delta Air Lines | 438 |
| 2 | American Airlines | 436 |
| 3 | United Airlines | 428 |
| 4 | Southwest Airlines | 423 |
| 5 | Ryanair | 332 |
| 6 | SkyWest Airlines | 215 |
| 7 | EJA | 167 |
| 8 | Alaska Airlines | 132 |
| 9 | Republic Airways | 119 |
| 10 | Turkish Airlines | 118 |
| 11 | JetBlue | 110 |
| 12 | Lufthansa | 97 |
| 13 | Air Canada | 96 |
| 14 | FFT | 91 |
| 15 | ENY | 90 |
| 16 | easyJet | 90 |
| 17 | Scandinavian Airlines | 75 |
| 18 | LXJ | 70 |
| 19 | WJA | 70 |
| 20 | EJU | 68 |
| 21 | Air France | 68 |
| 22 | EXS | 66 |
| 23 | British Airways | 63 |
| 24 | EDV | 62 |
| 25 | AAY | 61 |
| 26 | JIA | 60 |
| 27 | CXK | 58 |
| 28 | KLM Royal Dutch | 55 |
| 29 | Vueling | 53 |
| 30 | NKS | 51 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 7089 |
| 2 | 🇨🇦 Canada | 446 |
| 3 | 🇬🇧 United Kingdom | 336 |
| 4 | 🇮🇪 Ireland | 273 |
| 5 | 🇹🇷 Turkey | 215 |
| 6 | 🇩🇪 Germany | 209 |
| 7 | 🏳️ Malta | 160 |
| 8 | 🇲🇽 Mexico | 145 |
| 9 | 🇪🇸 Spain | 139 |
| 10 | 🇫🇷 France | 129 |
| 11 | 🇨🇳 China | 118 |
| 12 | 🇧🇷 Brazil | 116 |
| 13 | 🇮🇳 India | 109 |
| 14 | 🇦🇹 Austria | 100 |
| 15 | 🏳️ Kingdom of the Netherlands | 81 |
| 16 | 🇵🇱 Poland | 80 |
| 17 | 🇸🇪 Sweden | 71 |
| 18 | 🇨🇭 Switzerland | 49 |
| 19 | 🏳️ Hungary | 43 |
| 20 | 🇵🇹 Portugal | 43 |
| 21 | 🇯🇵 Japan | 42 |
| 22 | 🇫🇮 Finland | 40 |
| 23 | 🏳️ Republic of Korea | 40 |
| 24 | 🇨🇱 Chile | 39 |
| 25 | 🇦🇪 United Arab Emirates | 39 |
| 26 | 🇹🇼 Taiwan | 36 |
| 27 | 🏳️ Greece | 33 |
| 28 | 🇳🇴 Norway | 32 |
| 29 | 🏳️ Morocco | 32 |
| 30 | 🇪🇬 Egypt | 32 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 31 |
| 2 | Toronto Pearson International Airport | Mississauga | CA | 25 |
| 3 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 25 |
| 4 | Phoenix Sky Harbor International Airport | Phoenix | US | 22 |
| 5 | John F Kennedy International Airport | New York | US | 20 |
| 6 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 18 |
| 7 | Calgary International Airport | Calgary | CA | 17 |
| 8 | San Francisco International Airport | San Francisco | US | 17 |
| 9 | Harry Reid International Airport | Las Vegas | US | 16 |
| 10 | Denver International Airport | Denver | US | 15 |
| 11 | Chicago O'Hare International Airport | Chicago | US | 15 |
| 12 | Austin-Bergstrom International Airport | Austin | US | 15 |
| 13 | Cancun International Airport | Cancun | MX | 14 |
| 14 | General Edward Lawrence Logan International Airport | Boston | US | 14 |
| 15 | El Dorado International Airport | Bogota | CO | 12 |
| 16 | Nashville International Airport | Nashville | US | 12 |
| 17 | San Diego International Airport | San Diego | US | 12 |
| 18 | Amsterdam Airport Schiphol | Amsterdam | NL | 11 |
| 19 | La Aurora Airport | Guatemala City | GT | 10 |
| 20 | Rocky Mountain Metro Airport | Denver | US | 10 |
| 21 | Los Angeles International Airport | Los Angeles | US | 10 |
| 22 | Laguardia Airport | New York | US | 10 |
| 23 | Washington Dulles International Airport | Washington | US | 9 |
| 24 | Berlin Brandenburg Airport | Berlin | DE | 8 |
| 25 | Vienna International Airport | Vienna | AT | 8 |
| 26 | London Gatwick Airport | London | GB | 8 |
| 27 | Orlando International Airport | Orlando | US | 8 |
| 28 | Vancouver International Airport | Richmond | CA | 8 |
| 29 | Indira Gandhi International Airport | New Delhi | IN | 7 |
| 30 | Chhatrapati Shivaji International Airport | Mumbai | IN | 7 |
| 31 | Witham Field | Stuart | US | 7 |
| 32 | Ted Stevens Anchorage International Airport | Anchorage | US | 7 |
| 33 | Sydney Kingsford Smith International Airport | Sydney | AU | 7 |
| 34 | Salt Lake City International Airport | Salt Lake City | US | 7 |
| 35 | North Las Vegas Airport | Las Vegas | US | 7 |
| 36 | Ronald Reagan Washington Ntl Airport | Washington | US | 7 |
| 37 | Oakland San Francisco Bay Airport | Oakland | US | 7 |
| 38 | Manchester Airport | Manchester | GB | 7 |
| 39 | Van Nuys Airport | Van Nuys | US | 6 |
| 40 | Scottsdale Airport | Scottsdale | US | 6 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 4 | 27m |
| 2 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 3 | 26m |
| 3 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 3 | 22m |
| 4 | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 2 | 32m |
| 5 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2 | 14m |
| 6 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2 | 27m |
| 7 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 2 | 14m |
| 8 | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2 | 12m |
| 9 | Lanseria Airport (FALA) | Newcastle Airport (FANC) | 1 | 24m |
| 10 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 1 | 21m |
| 11 | Moi Air Base (HKRE) | Naivasha Airport (HKNV) | 1 | 6m |
| 12 | Blaise Diagne International Airport (GOBD) | Kawass Airport (GUKR) | 1 | 41m |
| 13 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 1 | 15m |
| 14 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 1 | 13m |
| 15 | Coban Airport (MGCB) | La Aurora Airport (MGGT) | 1 | 26m |
| 16 | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 1 | 19m |
| 17 | Lisbon Portela Airport (LPPT) | Vitoria/Foronda Airport (LEVT) | 1 | 53m |
| 18 | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 1 | 55m |
| 19 | Tenerife Norte Airport (GCXO) | Gran Canaria Airport (GCLP) | 1 | 18m |
| 20 | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 1 | 51m |
| 21 | Dusseldorf International Airport (EDDL) | Grobnicko Polje Airport (LDRG) | 1 | 1h 22m |
| 22 | Frankfurt am Main International Airport (EDDF) | Langhennersdorf Airport (EDOH) | 1 | 41m |
| 23 | Frankfurt am Main International Airport (EDDF) | Capua Airport (LIAU) | 1 | 1h 20m |
| 24 | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 1 | 14h 39m |
| 25 | London Heathrow Airport (EGLL) | Hamburg Airport (EDDH) | 1 | 1h 6m |
| 26 | London Gatwick Airport (EGKK) | Hoefen Airport (LOIR) | 1 | 1h 24m |
| 27 | London Stansted Airport (EGSS) | Visoko Sport Airfield (LQVI) | 1 | 1h 54m |
| 28 | Oslo Gardermoen Airport (ENGM) | Macau International Airport (VMMC) | 1 | 18h 53m |
| 29 | Amsterdam Airport Schiphol (EHAM) | Malpensa International Airport (LIMC) | 1 | 1h 27m |
| 30 | London Gatwick Airport (EGKK) | Capua Airport (LIAU) | 1 | 1h 56m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N429CF |  | Dallas Executive Airport (KRBD) | Baum Airport (TA46) | 2026-03-28 17:54 UTC | 2026-03-28 18:16 UTC | 21m |
| N6796H |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Christensen Ranch Airport (9CL2) | 2026-03-28 17:51 UTC | 2026-03-28 18:16 UTC | 25m |
| N561ND |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-03-28 17:30 UTC | 2026-03-28 18:05 UTC | 34m |
| N797NA |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-03-28 17:38 UTC | 2026-03-28 18:05 UTC | 26m |
| N75SM |  | Salida/Harriett Alexander Field (KANK) | Salida/Harriett Alexander Field (KANK) | 2026-03-28 17:44 UTC | 2026-03-28 18:02 UTC | 17m |
| LY620 |  | Santa Rosa Nolf Airport (KNGS) | Santa Rosa Nolf Airport (KNGS) | 2026-03-28 17:49 UTC | 2026-03-28 18:00 UTC | 10m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-03-28 17:43 UTC | 2026-03-28 17:56 UTC | 12m |
| N820DM |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-03-28 17:49 UTC | 2026-03-28 17:50 UTC | 1m |
| N2936Q |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-03-28 17:44 UTC | 2026-03-28 17:49 UTC | 4m |
| HK1479G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-03-28 17:22 UTC | 2026-03-28 17:48 UTC | 26m |
| N82EM |  | Space Florida Launch And Landing Facility Airport (KTTS) | Lehigh Valley International Airport (KABE) | 2026-03-28 15:48 UTC | 2026-03-28 17:48 UTC | 1h 59m |
| BOE842 | BOE | Seattle Paine Field International Airport (KPAE) | Warden Airport (K2S4) | 2026-03-28 16:17 UTC | 2026-03-28 17:47 UTC | 1h 29m |
| N5403H |  | Denton Enterprise Airport (KDTO) | Jbj Ranch Airport (XA98) | 2026-03-28 17:20 UTC | 2026-03-28 17:44 UTC | 24m |
|  |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-03-28 17:20 UTC | 2026-03-28 17:43 UTC | 23m |
| CXK470 | CXK | Indy South Greenwood Airport (KHFY) | Indy South Greenwood Airport (KHFY) | 2026-03-28 17:37 UTC | 2026-03-28 17:43 UTC | 6m |
| N521NG |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-03-28 17:06 UTC | 2026-03-28 17:41 UTC | 35m |
| N55DB |  | Carson City Airport (KCXP) | Dayton Valley Airpark (KA34) | 2026-03-28 17:22 UTC | 2026-03-28 17:37 UTC | 15m |
| SAS757 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Cewice Military Airport (EPCE) | 2026-03-28 16:49 UTC | 2026-03-28 17:36 UTC | 47m |
| N559BG |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-03-28 17:13 UTC | 2026-03-28 17:36 UTC | 22m |
| ASA495 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Bermuda Dunes Airport (KUDD) | 2026-03-28 15:24 UTC | 2026-03-28 17:35 UTC | 2h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
