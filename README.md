# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_20:46:35_UTC-green)

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

**2026-03-28 20:46:35 UTC**

- **10,150** aircraft tracked
- **9,335** currently in the air
- **815** on the ground
- **97** countries
- **100** airports with traffic
- **50** airlines identified
- **180** flight routes (last 2h)
- **1h 12m** average flight duration

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Southwest Airlines | 449 |
| 2 | American Airlines | 444 |
| 3 | Delta Air Lines | 435 |
| 4 | United Airlines | 409 |
| 5 | Ryanair | 329 |
| 6 | SkyWest Airlines | 205 |
| 7 | EJA | 144 |
| 8 | JetBlue | 128 |
| 9 | Republic Airways | 117 |
| 10 | Alaska Airlines | 113 |
| 11 | ENY | 95 |
| 12 | Air Canada | 94 |
| 13 | easyJet | 91 |
| 14 | FFT | 88 |
| 15 | Lufthansa | 84 |
| 16 | EJU | 77 |
| 17 | WJA | 77 |
| 18 | AAY | 77 |
| 19 | LXJ | 74 |
| 20 | Air France | 74 |
| 21 | KLM Royal Dutch | 71 |
| 22 | Scandinavian Airlines | 65 |
| 23 | EDV | 62 |
| 24 | CXK | 57 |
| 25 | Vueling | 56 |
| 26 | Turkish Airlines | 56 |
| 27 | JIA | 54 |
| 28 | British Airways | 47 |
| 29 | NKS | 47 |
| 30 | Swiss International | 41 |

## Top Countries (by aircraft registration)

| # | Country | Aircraft |
|---:|---------|--------:|
| 1 | 🇺🇸 United States | 6467 |
| 2 | 🇨🇦 Canada | 451 |
| 3 | 🇬🇧 United Kingdom | 268 |
| 4 | 🇮🇪 Ireland | 244 |
| 5 | 🇩🇪 Germany | 173 |
| 6 | 🇪🇸 Spain | 161 |
| 7 | 🇹🇷 Turkey | 147 |
| 8 | 🇫🇷 France | 144 |
| 9 | 🇲🇽 Mexico | 143 |
| 10 | 🏳️ Malta | 142 |
| 11 | 🇦🇺 Australia | 127 |
| 12 | 🇨🇳 China | 113 |
| 13 | 🇦🇹 Austria | 107 |
| 14 | 🇧🇷 Brazil | 107 |
| 15 | 🏳️ Kingdom of the Netherlands | 98 |
| 16 | 🇵🇱 Poland | 76 |
| 17 | 🇨🇭 Switzerland | 73 |
| 18 | 🇸🇪 Sweden | 72 |
| 19 | 🇮🇳 India | 55 |
| 20 | 🏳️ Republic of Korea | 53 |
| 21 | 🇦🇪 United Arab Emirates | 52 |
| 22 | 🇯🇵 Japan | 49 |
| 23 | 🇳🇿 New Zealand | 48 |
| 24 | 🇹🇭 Thailand | 44 |
| 25 | 🏳️ Hungary | 43 |
| 26 | 🇵🇹 Portugal | 37 |
| 27 | 🇳🇴 Norway | 32 |
| 28 | 🏳️ Viet Nam | 32 |
| 29 | 🇸🇬 Singapore | 29 |
| 30 | 🇫🇮 Finland | 28 |

## Busiest Airports (aircraft on ground)

| # | Airport | City | Country | Aircraft |
|---:|---------|------|---------|--------:|
| 1 | Hartsfield/Jackson Atlanta International Airport | Atlanta | US | 31 |
| 2 | Dallas-Fort Worth International Airport | Dallas-Fort Worth | US | 27 |
| 3 | Sydney Kingsford Smith International Airport | Sydney | AU | 25 |
| 4 | Toronto Pearson International Airport | Mississauga | CA | 22 |
| 5 | Zurich Airport | Zurich | CH | 22 |
| 6 | Orlando International Airport | Orlando | US | 18 |
| 7 | Frankfurt am Main International Airport | Frankfurt am Main | DE | 18 |
| 8 | General Edward Lawrence Logan International Airport | Boston | US | 18 |
| 9 | Vancouver International Airport | Richmond | CA | 17 |
| 10 | Harry Reid International Airport | Las Vegas | US | 17 |
| 11 | John F Kennedy International Airport | New York | US | 16 |
| 12 | Laguardia Airport | New York | US | 16 |
| 13 | Chicago O'Hare International Airport | Chicago | US | 15 |
| 14 | Phoenix Sky Harbor International Airport | Phoenix | US | 15 |
| 15 | Newark Liberty International Airport | Newark | US | 14 |
| 16 | Cancun International Airport | Cancun | MX | 13 |
| 17 | Amsterdam Airport Schiphol | Amsterdam | NL | 12 |
| 18 | London Gatwick Airport | London | GB | 12 |
| 19 | Norman Y Mineta San Jose International Airport | San Jose | US | 11 |
| 20 | Nashville International Airport | Nashville | US | 11 |
| 21 | Washington Dulles International Airport | Washington | US | 11 |
| 22 | Calgary International Airport | Calgary | CA | 10 |
| 23 | San Francisco International Airport | San Francisco | US | 10 |
| 24 | Paris-Orly Airport | Paris | FR | 10 |
| 25 | Denver International Airport | Denver | US | 10 |
| 26 | Tokyo International Airport | Tokyo | JP | 10 |
| 27 | Rocky Mountain Metro Airport | Denver | US | 9 |
| 28 | Tampa International Airport | Tampa | US | 9 |
| 29 | El Dorado International Airport | Bogota | CO | 8 |
| 30 | Salt Lake City International Airport | Salt Lake City | US | 8 |
| 31 | Oakland San Francisco Bay Airport | Oakland | US | 8 |
| 32 | San Diego International Airport | San Diego | US | 7 |
| 33 | Los Angeles International Airport | Los Angeles | US | 7 |
| 34 | Austin-Bergstrom International Airport | Austin | US | 7 |
| 35 | Melbourne International Airport | Melbourne | AU | 7 |
| 36 | Scottsdale Airport | Scottsdale | US | 7 |
| 37 | General Mariano Escobedo International Airport | Monterrey | MX | 6 |
| 38 | Vienna International Airport | Vienna | AT | 6 |
| 39 | Teterboro Airport | Teterboro | US | 6 |
| 40 | Southwest Florida International Airport | Fort Myers | US | 6 |

## Top Routes (last 2 hours)

| # | From | To | Flights | Avg Duration |
|---:|------|-----|--------:|------------:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2 | 32m |
| 2 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2 | 20m |
| 3 | KU42 (KU42) | Wendover Airport (KENV) | 2 | 48m |
| 4 | Scottsdale Airport (KSDL) | Rimrock Airport (48AZ) | 2 | 22m |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 2 | 14m |
| 6 | Melsbroek Air Base (EBMB) | Nador International Airport (GMMW) | 1 | 2h 18m |
| 7 | El Dorado International Airport (SKBO) | Melgar Air Base (SKME) | 1 | 17m |
| 8 | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 1 | 11m |
| 9 | El Dorado International Airport (SKBO) | Tunja Airport (SKTJ) | 1 | 13m |
| 10 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 1 | 10m |
| 11 | La Aurora Airport (MGGT) | La America Airport (MHEI) | 1 | 37m |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 1 | 26m |
| 13 | Santa Cruz del Quiche Airport (MGQC) | La Aurora Airport (MGGT) | 1 | 28m |
| 14 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 1 | 19m |
| 15 | Francisco Sarabia International Airport (MMTC) | Atizapan De Zaragoza Airport (MMJC) | 1 | 1h 4m |
| 16 | Palma De Mallorca Airport (LEPA) | Leon Airport (LELN) | 1 | 1h 7m |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 1 | 28m |
| 18 | La Palma Airport (GCLA) | Tenerife Norte Airport (GCXO) | 1 | 12m |
| 19 | Bremen Airport (EDDW) | Frankfurt am Main International Airport (EDDF) | 1 | 40m |
| 20 | Cumbernauld Airport (EGPG) | Glasgow International Airport (EGPF) | 1 | 27m |
| 21 | Glasgow International Airport (EGPF) | Glasgow International Airport (EGPF) | 1 | 3m |
| 22 | London Stansted Airport (EGSS) | Dubrovnik Airport (LDDU) | 1 | 2h 3m |
| 23 | Vienna International Airport (LOWW) | Linate Airport (LIML) | 1 | 1h 7m |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 1 | 21m |
| 25 | Oslo Gardermoen Airport (ENGM) | Pristina International Airport (BKPR) | 1 | 2h 41m |
| 26 | Warsaw Chopin Airport (EPWA) | Malpensa International Airport (LIMC) | 1 | 1h 48m |
| 27 | Paris Beauvais Tille Airport (LFOB) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 1 | 1h 50m |
| 28 | Copenhagen Kastrup Airport (EKCH) | Chania International Airport (LGSA) | 1 | 2h 55m |
| 29 | Geneva Cointrin International Airport (LSGG) | Zurich Airport (LSZH) | 1 | 28m |
| 30 | London Luton Airport (EGGW) | Karain Airport (LTXE) | 1 | 3h 31m |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N528TH |  | Addison Airport (KADS) | 0TX8 (0TX8) | 2026-03-28 19:41 UTC | 2026-03-28 20:29 UTC | 48m |
| BYF31 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-03-28 19:45 UTC | 2026-03-28 20:22 UTC | 36m |
| N6440J |  | Northwest Alabama Regional Airport (KMSL) | Wilson Creek Airport (0AL9) | 2026-03-28 20:08 UTC | 2026-03-28 20:19 UTC | 11m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-03-28 06:10 UTC | 2026-03-28 20:18 UTC | 14h 8m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-28 05:56 UTC | 2026-03-28 20:17 UTC | 14h 21m |
| N24AS |  | North Las Vegas Airport (KVGT) | KU42 (KU42) | 2026-03-28 18:19 UTC | 2026-03-28 20:16 UTC | 1h 56m |
|  |  | Columbus Airport (KCSG) | Columbus Airport (KCSG) | 2026-03-28 20:14 UTC | 2026-03-28 20:14 UTC | 0m |
| BRCAT04 | BRC | Cavern City Air Trml Airport (KCNM) | Cavern City Air Trml Airport (KCNM) | 2026-03-28 19:50 UTC | 2026-03-28 20:14 UTC | 23m |
| N609TS |  | Creve Coeur Airport (K1H0) | Blackhawk Airport (6MO0) | 2026-03-28 20:07 UTC | 2026-03-28 20:13 UTC | 6m |
| CXK184 | CXK | Riverside Airport (KRAL) | Van Nuys Airport (KVNY) | 2026-03-28 19:23 UTC | 2026-03-28 20:11 UTC | 48m |
| XSN06 | XSN | Napa County Airport (KAPC) | North Las Vegas Airport (KVGT) | 2026-03-28 18:44 UTC | 2026-03-28 20:09 UTC | 1h 25m |
| N157U |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-03-28 19:28 UTC | 2026-03-28 20:07 UTC | 39m |
| N51580 |  | Middletown Regional/Hook Field (KMWO) | Richmond Municipal Airport (KRID) | 2026-03-28 19:41 UTC | 2026-03-28 20:06 UTC | 25m |
| PDU56 | PDU | Vermilion Regional Airport (KDNV) | Purdue University Airport (KLAF) | 2026-03-28 19:37 UTC | 2026-03-28 20:06 UTC | 29m |
| N651AD |  | Scottsdale Airport (KSDL) | Rimrock Airport (48AZ) | 2026-03-28 19:45 UTC | 2026-03-28 20:06 UTC | 21m |
| TGCYC | TGC | Santa Cruz del Quiche Airport (MGQC) | La Aurora Airport (MGGT) | 2026-03-28 19:38 UTC | 2026-03-28 20:06 UTC | 28m |
| N110UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-03-28 18:58 UTC | 2026-03-28 20:05 UTC | 1h 6m |
| BRCAT15 | BRC | Jenkins Airport (NM87) | Artesia Municipal Airport (KATS) | 2026-03-28 19:23 UTC | 2026-03-28 20:03 UTC | 40m |
| N546CA |  | Montgomery-Gibbs Executive Airport (KMYF) | San Bernardino International Airport (KSBD) | 2026-03-28 18:59 UTC | 2026-03-28 20:02 UTC | 1h 3m |
| N815DS |  | Skypark Airport (KBTF) | Malad City Airport (KMLD) | 2026-03-28 19:17 UTC | 2026-03-28 20:02 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
