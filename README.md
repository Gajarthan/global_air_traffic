# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_22:14:17_UTC-green)

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

**2026-03-28 22:14:17 UTC**

- **8,972** aircraft tracked
- **8,219** currently in the air
- **753** on the ground
- **92** countries
- **100** airports with traffic
- **50** airlines identified
- **158** flight routes (last 2h)
- **1h 21m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Delta Air Lines | 496 |
| 2 | Southwest Airlines | 469 |
| 3 | United Airlines | 464 |
| 4 | American Airlines | 454 |
| 5 | Ryanair | 254 |
| 6 | SkyWest Airlines | 198 |
| 7 | EJA | 132 |
| 8 | JetBlue | 127 |
| 9 | Alaska Airlines | 117 |
| 10 | Republic Airways | 101 |
| 11 | Air Canada | 95 |
| 12 | ENY | 94 |
| 13 | FFT | 93 |
| 14 | easyJet | 89 |
| 15 | WJA | 72 |
| 16 | JIA | 69 |
| 17 | LXJ | 64 |
| 18 | AAY | 61 |
| 19 | Lufthansa | 58 |
| 20 | EDV | 56 |
| 21 | NKS | 53 |
| 22 | LATAM Airlines | 49 |
| 23 | UPS | 46 |
| 24 | EXS | 40 |
| 25 | Vueling | 39 |
| 26 | TAP Air Portugal | 39 |
| 27 | CXK | 38 |
| 28 | Scandinavian Airlines | 35 |
| 29 | EJU | 35 |
| 30 | JST | 34 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 5964 |
| 2 | 🇨🇦 Canada | 390 |
| 3 | 🇬🇧 United Kingdom | 226 |
| 4 | 🇦🇺 Australia | 215 |
| 5 | 🇮🇪 Ireland | 192 |
| 6 | 🇲🇽 Mexico | 121 |
| 7 | 🏳️ Malta | 108 |
| 8 | 🇩🇪 Germany | 105 |
| 9 | 🇧🇷 Brazil | 103 |
| 10 | 🇨🇳 China | 94 |
| 11 | 🇹🇷 Turkey | 91 |
| 12 | 🇪🇸 Spain | 88 |
| 13 | 🇯🇵 Japan | 88 |
| 14 | 🏳️ Republic of Korea | 76 |
| 15 | 🇳🇿 New Zealand | 70 |
| 16 | 🇦🇪 United Arab Emirates | 52 |
| 17 | 🇫🇷 France | 49 |
| 18 | 🇵🇱 Poland | 49 |
| 19 | 🏳️ Kingdom of the Netherlands | 46 |
| 20 | 🇮🇳 India | 44 |
| 21 | 🇸🇪 Sweden | 42 |
| 22 | 🇸🇬 Singapore | 41 |
| 23 | 🇦🇹 Austria | 40 |
| 24 | 🇹🇭 Thailand | 40 |
| 25 | 🇵🇹 Portugal | 40 |
| 26 | 🇨🇭 Switzerland | 38 |
| 27 | 🇨🇱 Chile | 37 |
| 28 | 🏳️ Hungary | 32 |
| 29 | 🇲🇾 Malaysia | 30 |
| 30 | 🇹🇼 Taiwan | 29 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 30 |
| 2 | General Edward Lawrence Logan International Airport | Boston | US | 24 |
| 3 | Denver International Airport | Denver | US | 22 |
| 4 | Calgary International Airport | Calgary | CA | 21 |
| 5 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 18 |
| 6 | Tokyo International Airport | Tokyo | JP | 17 |
| 7 | Toronto Pearson International Airport | Mississauga | CA | 17 |
| 8 | Washington Dulles International Airport | Washington | US | 16 |
| 9 | Phoenix Sky Harbor International Airport | Phoenix | US | 15 |
| 10 | Cancun International Airport | Cancun | MX | 15 |
| 11 | Harry Reid International Airport | Las Vegas | US | 15 |
| 12 | Sydney Kingsford Smith International Airport | Sydney | AU | 15 |
| 13 | San Francisco International Airport | San Francisco | US | 14 |
| 14 | Newark Liberty International Airport | Newark | US | 14 |
| 15 | Salt Lake City International Airport | Salt Lake City | US | 12 |
| 16 | Southwest Florida International Airport | Fort Myers | US | 12 |
| 17 | Nashville International Airport | Nashville | US | 12 |
| 18 | Tampa International Airport | Tampa | US | 11 |
| 19 | Laguardia Airport | New York | US | 11 |
| 20 | John F Kennedy International Airport | New York | US | 11 |
| 21 | Los Angeles International Airport | Los Angeles | US | 11 |
| 22 | Zurich Airport | Zurich | CH | 11 |
| 23 | Orlando International Airport | Orlando | US | 10 |
| 24 | San Diego International Airport | San Diego | US | 10 |
| 25 | Melbourne International Airport | Melbourne | AU | 10 |
| 26 | El Dorado International Airport | Bogota | CO | 9 |
| 27 | Chicago O'Hare International Airport | Chicago | US | 9 |
| 28 | London Gatwick Airport | London | GB | 9 |
| 29 | Austin-Bergstrom International Airport | Austin | US | 8 |
| 30 | Scottsdale Airport | Scottsdale | US | 7 |
| 31 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 7 |
| 32 | Chek Lap Kok International Airport | Hong Kong | HK | 7 |
| 33 | Brisbane International Airport | Brisbane | AU | 6 |
| 34 | Auburn University Regional Airport | Auburn | US | 6 |
| 35 | Gimpo International Airport | Seoul | KR | 6 |
| 36 | Jorge Newbery Airpark | Buenos Aires | AR | 5 |
| 37 | Vancouver International Airport | Richmond | CA | 5 |
| 38 | St Louis Lambert International Airport | St Louis | US | 5 |
| 39 | Ted Stevens Anchorage International Airport | Anchorage | US | 5 |
| 40 | San Carlos Airport | San Carlos | US | 5 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2 | 24m |
| 2 | Miami International Airport (KMIA) | The Florida Keys Marathon International Airport (KMTH) | 2 | 20m |
| 3 | Rafael Nunez International Airport (SKCG) | Alfonso Lopez Pumarejo Airport (SKVP) | 1 | 19m |
| 4 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 1 | 13m |
| 5 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1 | 27m |
| 6 | Santa Cruz del Quiche Airport (MGQC) | La Aurora Airport (MGGT) | 1 | 28m |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 1 | 21m |
| 8 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 0m |
| 9 | Madrid Barajas International Airport (LEMD) | Lanzarote Airport (GCRR) | 1 | 1h 58m |
| 10 | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 1 | 1h 14m |
| 11 | Barcelona International Airport (LEBL) | Napoli / Capodichino International Airport (LIRN) | 1 | 1h 16m |
| 12 | Alicante International Airport (LEAL) | Mostaganem Airport (DA14) | 1 | 24m |
| 13 | London Stansted Airport (EGSS) | Tivat Airport (LYTV) | 1 | 2h 6m |
| 14 | Václav Havel Airport (LKPR) | Niksic Airport (LYNK) | 1 | 1h 9m |
| 15 | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 1 | 1h 6m |
| 16 | Brussels South Charleroi Airport (EBCI) | Ifrane Airport (GMFI) | 1 | 2h 24m |
| 17 | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 1 | 1h 5m |
| 18 | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 1 | 38m |
| 19 | Riga International Airport (EVRA) | Zurich Airport (LSZH) | 1 | 2h 18m |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 1 | 32m |
| 21 | Nagasaki Airport (RJFU) | Takamatsu Airport (RJOT) | 1 | 26m |
| 22 | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 1 | 14h 8m |
| 23 | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 1 | 14h 21m |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 1 | 52m |
| 25 | London Gatwick Airport (EGKK) | Fujairah International Airport (OMFJ) | 1 | 6h 39m |
| 26 | Charles de Gaulle International Airport (LFPG) | Fujairah International Airport (OMFJ) | 1 | 6h 25m |
| 27 | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 1 | 1h 6m |
| 28 | Midland International Air And Space Port Airport (KMAF) | Andrews County Airport (KE11) | 1 | 12m |
| 29 | Provo Municipal Airport (KPVU) | K36U (K36U) | 1 | 11m |
| 30 | Modesto City-County-Harry Sham Field (KMOD) | Lake Tahoe Airport (KTVL) | 1 | 34m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N65641 |  | Blue Grass Airport (KLEX) | Georgetown-Scott County Regional Airport (K27K) | 2026-03-28 21:45 UTC | 2026-03-28 21:58 UTC | 13m |
| N350BV |  | Meadows Field (KBFL) | Van Nuys Airport (KVNY) | 2026-03-28 21:37 UTC | 2026-03-28 21:56 UTC | 19m |
| N541LC |  | Daniel K Inouye International Airport (PHNL) | Lanai Airport (PHNY) | 2026-03-28 20:59 UTC | 2026-03-28 21:53 UTC | 54m |
| N1718A |  | Julian Hinds Pump Plant Airstrip (73CL) | Henderson Executive Airport (KHND) | 2026-03-28 21:20 UTC | 2026-03-28 21:47 UTC | 27m |
| N448LF |  | Fountains Airport (ID60) | Felts Field (KSFF) | 2026-03-28 21:15 UTC | 2026-03-28 21:43 UTC | 28m |
| N442KS |  | Atlanta Regional Falcon Field (KFFC) | K4A7 (K4A7) | 2026-03-28 21:07 UTC | 2026-03-28 21:41 UTC | 33m |
| N229DM |  | Dodge County Airport (KUNU) | Watertown Municipal Airport (KRYV) | 2026-03-28 21:13 UTC | 2026-03-28 21:41 UTC | 27m |
| N264SF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-03-28 21:14 UTC | 2026-03-28 21:40 UTC | 26m |
| N955TX |  | Lubbock Preston Smith International Airport (KLBB) | Andrews County Airport (KE11) | 2026-03-28 21:19 UTC | 2026-03-28 21:38 UTC | 19m |
| N508XC |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-03-28 20:54 UTC | 2026-03-28 21:36 UTC | 41m |
| N212CP |  | Allegheny County Airport (KAGC) | Grant County Airport (KW99) | 2026-03-28 20:04 UTC | 2026-03-28 21:32 UTC | 1h 28m |
| SWR5717 | Swiss International | Riga International Airport (EVRA) | Zurich Airport (LSZH) | 2026-03-28 19:13 UTC | 2026-03-28 21:32 UTC | 2h 18m |
| N291VK |  | Youngberg Ranch Airport (NV17) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-03-28 20:47 UTC | 2026-03-28 21:30 UTC | 42m |
| N53176 |  | John Wayne/Orange County Airport (KSNA) | John Wayne/Orange County Airport (KSNA) | 2026-03-28 21:15 UTC | 2026-03-28 21:29 UTC | 14m |
| N9547W |  | Ogden-Hinckley Airport (KOGD) | Nephi Municipal Airport (KU14) | 2026-03-28 20:32 UTC | 2026-03-28 21:29 UTC | 56m |
| N918SA |  | Oxnard Airport (KOXR) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-03-28 21:05 UTC | 2026-03-28 21:28 UTC | 22m |
| BRCAT20 | BRC | Roswell Air Center Airport (KROW) | Double V Ranch Airport (NM38) | 2026-03-28 20:43 UTC | 2026-03-28 21:27 UTC | 44m |
| N216DG |  | 53TX (53TX) | T-Ranch Airport (XS86) | 2026-03-28 20:55 UTC | 2026-03-28 21:26 UTC | 31m |
| UPS22 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-03-28 09:57 UTC | 2026-03-28 21:24 UTC | 11h 27m |
| N332X |  | Mc Minnville Municipal Airport (KMMV) | Mc Minnville Municipal Airport (KMMV) | 2026-03-28 20:10 UTC | 2026-03-28 21:20 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
