# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_21:48:55_UTC-green)

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

**2026-03-28 21:48:55 UTC**

- **9,302** aircraft tracked
- **8,489** currently in the air
- **813** on the ground
- **95** countries
- **100** airports with traffic
- **50** airlines identified
- **158** flight routes (last 2h)
- **1h 32m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Delta Air Lines | 469 |
| 2 | American Airlines | 450 |
| 3 | United Airlines | 445 |
| 4 | Southwest Airlines | 444 |
| 5 | Ryanair | 284 |
| 6 | SkyWest Airlines | 204 |
| 7 | EJA | 134 |
| 8 | JetBlue | 121 |
| 9 | Republic Airways | 108 |
| 10 | Alaska Airlines | 103 |
| 11 | easyJet | 94 |
| 12 | FFT | 90 |
| 13 | Air Canada | 87 |
| 14 | ENY | 82 |
| 15 | Lufthansa | 81 |
| 16 | WJA | 74 |
| 17 | AAY | 73 |
| 18 | NKS | 59 |
| 19 | LXJ | 57 |
| 20 | EDV | 56 |
| 21 | UPS | 54 |
| 22 | JIA | 53 |
| 23 | LATAM Airlines | 45 |
| 24 | EXS | 45 |
| 25 | EJU | 44 |
| 26 | KLM Royal Dutch | 44 |
| 27 | Vueling | 42 |
| 28 | Turkish Airlines | 41 |
| 29 | Aeromexico | 40 |
| 30 | Air France | 40 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 6125 |
| 2 | 🇨🇦 Canada | 396 |
| 3 | 🇬🇧 United Kingdom | 253 |
| 4 | 🇮🇪 Ireland | 214 |
| 5 | 🇦🇺 Australia | 183 |
| 6 | 🇩🇪 Germany | 142 |
| 7 | 🏳️ Malta | 125 |
| 8 | 🇹🇷 Turkey | 121 |
| 9 | 🇲🇽 Mexico | 115 |
| 10 | 🇪🇸 Spain | 108 |
| 11 | 🇧🇷 Brazil | 107 |
| 12 | 🇨🇳 China | 104 |
| 13 | 🏳️ Republic of Korea | 78 |
| 14 | 🇫🇷 France | 76 |
| 15 | 🇯🇵 Japan | 64 |
| 16 | 🏳️ Kingdom of the Netherlands | 62 |
| 17 | 🇨🇭 Switzerland | 61 |
| 18 | 🇮🇳 India | 55 |
| 19 | 🇳🇿 New Zealand | 54 |
| 20 | 🇦🇪 United Arab Emirates | 54 |
| 21 | 🇦🇹 Austria | 53 |
| 22 | 🇵🇱 Poland | 50 |
| 23 | 🇸🇪 Sweden | 47 |
| 24 | 🇸🇬 Singapore | 41 |
| 25 | 🏳️ Hungary | 39 |
| 26 | 🇵🇹 Portugal | 39 |
| 27 | 🇹🇭 Thailand | 35 |
| 28 | 🇨🇱 Chile | 34 |
| 29 | 🇳🇴 Norway | 27 |
| 30 | 🇹🇼 Taiwan | 25 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 26 |
| 2 | Washington Dulles International Airport | Washington | US | 26 |
| 3 | Phoenix Sky Harbor International Airport | Phoenix | US | 24 |
| 4 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 23 |
| 5 | Sydney Kingsford Smith International Airport | Sydney | AU | 22 |
| 6 | Zurich Airport | Zurich | CH | 21 |
| 7 | General Edward Lawrence Logan International Airport | Boston | US | 20 |
| 8 | Orlando International Airport | Orlando | US | 18 |
| 9 | Newark Liberty International Airport | Newark | US | 17 |
| 10 | Chicago O'Hare International Airport | Chicago | US | 16 |
| 11 | Toronto Pearson International Airport | Mississauga | CA | 16 |
| 12 | Cancun International Airport | Cancun | MX | 15 |
| 13 | Calgary International Airport | Calgary | CA | 14 |
| 14 | Los Angeles International Airport | Los Angeles | US | 14 |
| 15 | Tokyo International Airport | Tokyo | JP | 14 |
| 16 | John F Kennedy International Airport | New York | US | 13 |
| 17 | San Francisco International Airport | San Francisco | US | 13 |
| 18 | Denver International Airport | Denver | US | 13 |
| 19 | Nashville International Airport | Nashville | US | 12 |
| 20 | Rocky Mountain Metro Airport | Denver | US | 12 |
| 21 | San Diego International Airport | San Diego | US | 11 |
| 22 | Norman Y Mineta San Jose International Airport | San Jose | US | 11 |
| 23 | Laguardia Airport | New York | US | 9 |
| 24 | Vienna International Airport | Vienna | AT | 9 |
| 25 | Vancouver International Airport | Richmond | CA | 9 |
| 26 | Salt Lake City International Airport | Salt Lake City | US | 9 |
| 27 | Montréal-Pierre Elliott Trudeau International Airport | Dorval | CA | 9 |
| 28 | Paris-Orly Airport | Paris | FR | 8 |
| 29 | Ted Stevens Anchorage International Airport | Anchorage | US | 8 |
| 30 | Portland International Airport | Portland | US | 8 |
| 31 | London Gatwick Airport | London | GB | 8 |
| 32 | Scottsdale Airport | Scottsdale | US | 8 |
| 33 | Austin-Bergstrom International Airport | Austin | US | 8 |
| 34 | Brisbane International Airport | Brisbane | AU | 8 |
| 35 | Southwest Florida International Airport | Fort Myers | US | 7 |
| 36 | Chek Lap Kok International Airport | Hong Kong | HK | 7 |
| 37 | St Louis Lambert International Airport | St Louis | US | 6 |
| 38 | Harry Reid International Airport | Las Vegas | US | 6 |
| 39 | Tampa International Airport | Tampa | US | 6 |
| 40 | Gimpo International Airport | Seoul | KR | 6 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | Athanasiou Valley Airport (CO07) | Athanasiou Valley Airport (CO07) | 2 | 20m |
| 2 | Scottsdale Airport (KSDL) | Rimrock Airport (48AZ) | 2 | 22m |
| 3 | Rafael Nunez International Airport (SKCG) | Alfonso Lopez Pumarejo Airport (SKVP) | 1 | 19m |
| 4 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 1 | 13m |
| 5 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1 | 27m |
| 6 | Santa Cruz del Quiche Airport (MGQC) | La Aurora Airport (MGGT) | 1 | 28m |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 1 | 21m |
| 8 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 1 | 19m |
| 9 | Xoxocotlan International Airport (MMOX) | Atizapan De Zaragoza Airport (MMJC) | 1 | 42m |
| 10 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 0m |
| 11 | Madrid Barajas International Airport (LEMD) | Lanzarote Airport (GCRR) | 1 | 1h 58m |
| 12 | Palma De Mallorca Airport (LEPA) | Leon Airport (LELN) | 1 | 1h 7m |
| 13 | Barcelona International Airport (LEBL) | Napoli / Capodichino International Airport (LIRN) | 1 | 1h 16m |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 1 | 33m |
| 15 | London Stansted Airport (EGSS) | Tivat Airport (LYTV) | 1 | 2h 6m |
| 16 | Copernicus Wrocław Airport (EPWR) | Newcastle Airport (EGNT) | 1 | 1h 49m |
| 17 | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 1 | 1h 6m |
| 18 | Geneva Cointrin International Airport (LSGG) | Brussels Airport (EBBR) | 1 | 55m |
| 19 | Antalya International Airport (LTAI) | Hodkovice Nad Mohelkou Airport (LKHD) | 1 | 2h 50m |
| 20 | London Luton Airport (EGGW) | Karain Airport (LTXE) | 1 | 3h 31m |
| 21 | Marseille Provence Airport (LFML) | Ifrane Airport (GMFI) | 1 | 1h 50m |
| 22 | Brussels South Charleroi Airport (EBCI) | Ifrane Airport (GMFI) | 1 | 2h 24m |
| 23 | Dublin Airport (EIDW) | Usti Nad Labem Airport (LKUL) | 1 | 2h 9m |
| 24 | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Brindisi / Casale Airport (LIBR) | 1 | 57m |
| 25 | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 1 | 1h 5m |
| 26 | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 1 | 38m |
| 27 | Nagasaki Airport (RJFU) | Takamatsu Airport (RJOT) | 1 | 26m |
| 28 | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 1 | 14h 8m |
| 29 | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 1 | 14h 21m |
| 30 | Suvarnabhumi Airport (VTBS) | Takamatsu Airport (RJOT) | 1 | 10h 5m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N955TX |  | Lubbock Preston Smith International Airport (KLBB) | Andrews County Airport (KE11) | 2026-03-28 21:19 UTC | 2026-03-28 21:38 UTC | 19m |
| N508XC |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-03-28 20:54 UTC | 2026-03-28 21:36 UTC | 41m |
| N53176 |  | John Wayne/Orange County Airport (KSNA) | John Wayne/Orange County Airport (KSNA) | 2026-03-28 21:15 UTC | 2026-03-28 21:29 UTC | 14m |
| N918SA |  | Oxnard Airport (KOXR) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-03-28 21:05 UTC | 2026-03-28 21:28 UTC | 22m |
| N216DG |  | 53TX (53TX) | T-Ranch Airport (XS86) | 2026-03-28 20:55 UTC | 2026-03-28 21:26 UTC | 31m |
| UPS22 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-03-28 09:57 UTC | 2026-03-28 21:24 UTC | 11h 27m |
| N332X |  | Mc Minnville Municipal Airport (KMMV) | Mc Minnville Municipal Airport (KMMV) | 2026-03-28 20:10 UTC | 2026-03-28 21:20 UTC | 1h 10m |
| UAE65W | Emirates | Charles de Gaulle International Airport (LFPG) | Fujairah International Airport (OMFJ) | 2026-03-28 14:50 UTC | 2026-03-28 21:15 UTC | 6h 25m |
| N871DG |  | Dallas Love Field (KDAL) | San Carlos Airport (KSQL) | 2026-03-28 12:15 UTC | 2026-03-28 21:14 UTC | 8h 58m |
| N2055E |  | Charlotte/Monroe Executive Airport (KEQY) | Brown Field (46NC) | 2026-03-28 20:56 UTC | 2026-03-28 21:12 UTC | 15m |
| UAE1CL | Emirates | London Gatwick Airport (EGKK) | Fujairah International Airport (OMFJ) | 2026-03-28 14:31 UTC | 2026-03-28 21:11 UTC | 6h 39m |
| N918BV |  | Indianapolis Executive Airport (KTYQ) | Indianapolis Executive Airport (KTYQ) | 2026-03-28 21:07 UTC | 2026-03-28 21:11 UTC | 3m |
| N4DW |  | Oxnard Airport (KOXR) | Mc Clellan-Palomar Airport (KCRQ) | 2026-03-28 20:21 UTC | 2026-03-28 21:09 UTC | 48m |
| N172RC |  | Denton Enterprise Airport (KDTO) | Tightwaad Air Ranch Airport (XA16) | 2026-03-28 19:43 UTC | 2026-03-28 21:08 UTC | 1h 25m |
| REH13 | REH | Hesperia Airport (KL26) | On The Rocks Airport (1CA6) | 2026-03-28 20:20 UTC | 2026-03-28 21:05 UTC | 45m |
| HTS068 | HTS | Rafael Nunez International Airport (SKCG) | Alfonso Lopez Pumarejo Airport (SKVP) | 2026-03-28 20:43 UTC | 2026-03-28 21:02 UTC | 19m |
| N75255 |  | Hennessy Airport (26FD) | Lake Wales Municipal Airport (KX07) | 2026-03-28 20:16 UTC | 2026-03-28 21:01 UTC | 45m |
| N491LG |  | Athanasiou Valley Airport (CO07) | Athanasiou Valley Airport (CO07) | 2026-03-28 20:44 UTC | 2026-03-28 20:54 UTC | 10m |
| EJA927 | EJA | Brunswick Golden Isles Airport (KBQK) | Salina Regional Airport (KSLN) | 2026-03-28 18:12 UTC | 2026-03-28 20:53 UTC | 2h 41m |
| N391LG |  | Tall Timber Airport (CD28) | Athanasiou Valley Airport (CO07) | 2026-03-28 20:30 UTC | 2026-03-28 20:48 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
