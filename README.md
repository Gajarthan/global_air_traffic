# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_19:56:02_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-04-15 19:56:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 19:56:02 UTC

- **36,460** saved flights
- **15,904** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **36,460** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **441,241.1 tonnes** estimated CO2 emissions
- **25,579,195 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1556 |
| 2 | SkyWest Airlines | 1441 |
| 3 | IndiGo | 906 |
| 4 | EJA | 620 |
| 5 | American Airlines | 615 |
| 6 | Southwest Airlines | 512 |
| 7 | ENY | 481 |
| 8 | AXM | 386 |
| 9 | Lufthansa | 383 |
| 10 | LATAM Airlines | 370 |
| 11 | Vueling | 369 |
| 12 | AZU | 324 |
| 13 | All Nippon Airways | 321 |
| 14 | Delta Air Lines | 309 |
| 15 | QLK | 302 |
| 16 | LXJ | 290 |
| 17 | Swiss International | 277 |
| 18 | WIF | 272 |
| 19 | AEE | 247 |
| 20 | easyJet | 242 |
| 21 | Alaska Airlines | 239 |
| 22 | EJU | 238 |
| 23 | VIV | 232 |
| 24 | Japan Airlines | 222 |
| 25 | Air France | 208 |
| 26 | EDV | 204 |
| 27 | United Airlines | 203 |
| 28 | GLO | 196 |
| 29 | AIQ | 191 |
| 30 | JetBlue | 191 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 28597 |
| 2 | 🇮🇳 IN | 2771 |
| 3 | 🇪🇸 ES | 2724 |
| 4 | 🇦🇺 AU | 2549 |
| 5 | 🇧🇷 BR | 2154 |
| 6 | 🇯🇵 JP | 1968 |
| 7 | 🇮🇹 IT | 1948 |
| 8 | 🇩🇪 DE | 1878 |
| 9 | 🇨🇴 CO | 1794 |
| 10 | 🇨🇦 CA | 1780 |
| 11 | 🇬🇧 GB | 1507 |
| 12 | 🇫🇷 FR | 1385 |
| 13 | 🇲🇽 MX | 1141 |
| 14 | 🇬🇷 GR | 1108 |
| 15 | 🇨🇭 CH | 1004 |
| 16 | 🇲🇾 MY | 930 |
| 17 | 🇳🇴 NO | 884 |
| 18 | 🇳🇿 NZ | 774 |
| 19 | 🇿🇦 ZA | 770 |
| 20 | 🇵🇭 PH | 687 |
| 21 | 🇹🇭 TH | 669 |
| 22 | 🇹🇷 TR | 664 |
| 23 | 🇬🇹 GT | 622 |
| 24 | 🇰🇷 KR | 611 |
| 25 | 🇵🇱 PL | 571 |
| 26 | 🇲🇦 MA | 461 |
| 27 | 🇳🇱 NL | 363 |
| 28 | 🇧🇸 BS | 353 |
| 29 | 🇲🇪 ME | 352 |
| 30 | 🇮🇩 ID | 345 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 864 |
| 2 | Tokyo International Airport |  | JP | 667 |
| 3 | El Dorado International Airport |  | CO | 638 |
| 4 | Denver International Airport |  | US | 615 |
| 5 | Indira Gandhi International Airport |  | IN | 589 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 545 |
| 7 | Harry Reid International Airport |  | US | 480 |
| 8 | La Aurora Airport |  | GT | 456 |
| 9 | Guaymaral Airport |  | CO | 454 |
| 10 | Zurich Airport |  | CH | 449 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 365 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 363 |
| 13 | Chicago O'Hare International Airport |  | US | 361 |
| 14 | Kuala Lumpur International Airport |  | MY | 361 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 340 |
| 17 | Madrid Barajas International Airport |  | ES | 331 |
| 18 | Charlotte/Douglas International Airport |  | US | 325 |
| 19 | Tenerife Norte Airport |  | ES | 325 |
| 20 | Bengaluru International Airport |  | IN | 323 |
| 21 | Macau International Airport |  | MO | 322 |
| 22 | Congonhas Airport |  | BR | 322 |
| 23 | Ninoy Aquino International Airport |  | PH | 318 |
| 24 | Malpensa International Airport |  | IT | 298 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 284 |
| 26 | Salt Lake City International Airport |  | US | 275 |
| 27 | Daniel K Inouye International Airport |  | US | 273 |
| 28 | Charles de Gaulle International Airport |  | FR | 272 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 257 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 255 |
| 32 | Reno/Tahoe International Airport |  | US | 251 |
| 33 | O. R. Tambo International Airport |  | ZA | 248 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 248 |
| 35 | Vitoria/Foronda Airport |  | ES | 241 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 239 |
| 37 | Barcelona International Airport |  | ES | 238 |
| 38 | Viracopos International Airport |  | BR | 227 |
| 39 | Don Mueang International Airport |  | TH | 226 |
| 40 | Seattle-Tacoma International Airport |  | US | 225 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 178 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 148 | 14m | 114 km | 290.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 104 | 1h 27m | 910 km | 1,632.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 96 | 19m | 165 km | 273.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 86 | 21m | 244 km | 362.1 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 80 | 27m | 275 km | 379.1 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 79 | 21m | 99 km | 135.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 69 | 31m | 369 km | 439.2 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 68 | 45m | 452 km | 530.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 60 | 52m | 556 km | 575.1 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 56 | 13m | 99 km | 96.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 52 | 26m | 215 km | 192.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HRD06 | HRD | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-04-15 19:04 UTC | 2026-04-15 19:56 UTC | 51m |
| SKULL81 | SKU | KE80 (KE80) | KE80 (KE80) | 2026-04-15 18:52 UTC | 2026-04-15 19:49 UTC | 56m |
| N1266U |  | Fort Worth Meacham International Airport (KFTW) | Carter-Norman Airport (TA87) | 2026-04-15 19:20 UTC | 2026-04-15 19:46 UTC | 26m |
| BURNY32 | BUR | Wichita Valley Airport (KF14) | 5TA4 (5TA4) | 2026-04-15 19:26 UTC | 2026-04-15 19:46 UTC | 19m |
| LXJ345 | LXJ | Chicago Executive Airport (KPWK) | Witham Field (KSUA) | 2026-04-15 17:12 UTC | 2026-04-15 19:40 UTC | 2h 28m |
| N4512L |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-04-15 19:24 UTC | 2026-04-15 19:39 UTC | 15m |
| DEVIL52 | DEV | Fort Clark Springs Airport (74TX) | Anacacho Ranch Airport (0XS7) | 2026-04-15 19:26 UTC | 2026-04-15 19:39 UTC | 12m |
| N412RK |  | Wausau Downtown Airport (KAUW) | Dubuque Regional Airport (KDBQ) | 2026-04-15 19:02 UTC | 2026-04-15 19:39 UTC | 36m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-15 19:22 UTC | 2026-04-15 19:39 UTC | 17m |
| GRIT22 | GRI | Ansbach-Petersdorf Airport (EDQF) | Bad Windsheim Airport (EDQB) | 2026-04-15 19:25 UTC | 2026-04-15 19:39 UTC | 13m |
| CXK287 | CXK | Baton Rouge Metro, Ryan Field (KBTR) | False River Regional Airport (KHZR) | 2026-04-15 19:04 UTC | 2026-04-15 19:36 UTC | 32m |
| N4117H |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-15 19:21 UTC | 2026-04-15 19:36 UTC | 14m |
| HYD171 | HYD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-04-15 18:37 UTC | 2026-04-15 19:28 UTC | 51m |
| RNGR851 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Corpus Christi Nas (Truax Field) Airport (KNGP) | 2026-04-15 18:51 UTC | 2026-04-15 19:27 UTC | 36m |
| CXK550 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-15 17:54 UTC | 2026-04-15 19:27 UTC | 1h 32m |
| PAT087 | PAT | Wheeler Army Air Field (PHHI) | Wheeler Army Air Field (PHHI) | 2026-04-15 19:07 UTC | 2026-04-15 19:26 UTC | 18m |
| N523GC |  | Worcester Regional Airport (KORH) | Hamilton Municipal Airport (KVGC) | 2026-04-15 18:54 UTC | 2026-04-15 19:25 UTC | 31m |
| RNGR870 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-04-15 18:57 UTC | 2026-04-15 19:24 UTC | 26m |
| VPCXM | VPC | Paris-Le Bourget Airport (LFPB) | Lyon Saint-Exupery Airport (LFLL) | 2026-04-15 18:33 UTC | 2026-04-15 19:19 UTC | 45m |
| PSNFA | PSN | Correntina Airport (SNTY) | Fazenda Recanto da Cachoeira Airport (SWKY) | 2026-04-15 18:06 UTC | 2026-04-15 19:16 UTC | 1h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
