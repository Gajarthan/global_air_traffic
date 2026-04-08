# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_07:23:15_UTC-green)

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

**Latest saved flight:** 2026-04-08 07:23:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 07:23:15 UTC

- **22,817** saved flights
- **11,168** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,817** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **282,067.2 tonnes** estimated CO2 emissions
- **16,351,723 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 971 |
| 2 | Ryanair | 938 |
| 3 | IndiGo | 642 |
| 4 | EJA | 422 |
| 5 | American Airlines | 419 |
| 6 | Southwest Airlines | 330 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 287 |
| 9 | Vueling | 237 |
| 10 | AXM | 230 |
| 11 | LATAM Airlines | 230 |
| 12 | QLK | 208 |
| 13 | All Nippon Airways | 206 |
| 14 | Delta Air Lines | 199 |
| 15 | LXJ | 189 |
| 16 | AZU | 181 |
| 17 | Swiss International | 164 |
| 18 | VIV | 162 |
| 19 | Japan Airlines | 159 |
| 20 | Alaska Airlines | 158 |
| 21 | easyJet | 149 |
| 22 | United Airlines | 147 |
| 23 | EJU | 145 |
| 24 | AEE | 141 |
| 25 | Avianca | 139 |
| 26 | WIF | 139 |
| 27 | EDV | 135 |
| 28 | AXB | 129 |
| 29 | Air France | 119 |
| 30 | ANZ | 117 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18001 |
| 2 | 🇮🇳 IN | 1942 |
| 3 | 🇪🇸 ES | 1751 |
| 4 | 🇦🇺 AU | 1705 |
| 5 | 🇯🇵 JP | 1290 |
| 6 | 🇧🇷 BR | 1284 |
| 7 | 🇨🇴 CO | 1181 |
| 8 | 🇮🇹 IT | 1147 |
| 9 | 🇩🇪 DE | 1132 |
| 10 | 🇨🇦 CA | 1025 |
| 11 | 🇬🇧 GB | 886 |
| 12 | 🇫🇷 FR | 823 |
| 13 | 🇲🇽 MX | 747 |
| 14 | 🇬🇷 GR | 645 |
| 15 | 🇨🇭 CH | 611 |
| 16 | 🇲🇾 MY | 538 |
| 17 | 🇿🇦 ZA | 492 |
| 18 | 🇳🇿 NZ | 488 |
| 19 | 🇳🇴 NO | 479 |
| 20 | 🇬🇹 GT | 467 |
| 21 | 🇹🇷 TR | 437 |
| 22 | 🇵🇭 PH | 433 |
| 23 | 🇰🇷 KR | 408 |
| 24 | 🇹🇭 TH | 359 |
| 25 | 🇵🇱 PL | 326 |
| 26 | 🇲🇦 MA | 270 |
| 27 | 🇧🇸 BS | 243 |
| 28 | 🇮🇩 ID | 237 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 226 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 550 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 432 |
| 4 | Denver International Airport |  | US | 407 |
| 5 | Indira Gandhi International Airport |  | IN | 391 |
| 6 | La Aurora Airport |  | GT | 322 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 310 |
| 8 | Harry Reid International Airport |  | US | 307 |
| 9 | Zurich Airport |  | CH | 273 |
| 10 | Frankfurt am Main International Airport |  | DE | 251 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Chicago O'Hare International Airport |  | US | 238 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 237 |
| 15 | Guaymaral Airport |  | CO | 236 |
| 16 | Bengaluru International Airport |  | IN | 220 |
| 17 | Charlotte/Douglas International Airport |  | US | 214 |
| 18 | Macau International Airport |  | MO | 213 |
| 19 | Madrid Barajas International Airport |  | ES | 202 |
| 20 | Tenerife Norte Airport |  | ES | 202 |
| 21 | Ninoy Aquino International Airport |  | PH | 198 |
| 22 | Kuala Lumpur International Airport |  | MY | 195 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 24 | Congonhas Airport |  | BR | 186 |
| 25 | Salt Lake City International Airport |  | US | 182 |
| 26 | Malpensa International Airport |  | IT | 179 |
| 27 | Daniel K Inouye International Airport |  | US | 177 |
| 28 | Reno/Tahoe International Airport |  | US | 175 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 30 | Charles de Gaulle International Airport |  | FR | 165 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 155 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 152 |
| 35 | Pune Airport |  | IN | 152 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 151 |
| 37 | Seattle-Tacoma International Airport |  | US | 149 |
| 38 | Vitoria/Foronda Airport |  | ES | 149 |
| 39 | Barcelona International Airport |  | ES | 146 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 108 | 1h 8m | 706 km | 1,314.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 87 | 24m | 225 km | 337.5 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 87 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 81 | 28m | 304 km | 424.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 69 | 1h 28m | 910 km | 1,082.8 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 62 | 1h 42m | 1,156 km | 1,236.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 54 | 19m | 165 km | 153.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 51 | 55m | 546 km | 480.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 45 | 31m | 369 km | 286.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 42 | 4m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 41 | 46m | 452 km | 319.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 39 | 1h 43m | 1,423 km | 957.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 33 | 1h 22m | 961 km | 547.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZES | ZES | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-08 06:34 UTC | 2026-04-08 07:23 UTC | 48m |
| AUR201 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-04-08 07:05 UTC | 2026-04-08 07:17 UTC | 12m |
| TWY206 | TWY | Boeing Field/King County International Airport (KBFI) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-08 05:25 UTC | 2026-04-08 07:01 UTC | 1h 36m |
| R21235 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-08 05:58 UTC | 2026-04-08 06:58 UTC | 1h 0m |
| UAL909 | United Airlines | Chicago O'Hare International Airport (KORD) | Amsterdam Airport Schiphol (EHAM) | 2026-04-07 23:14 UTC | 2026-04-08 06:52 UTC | 7h 38m |
| NOZ42U | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-04-08 06:09 UTC | 2026-04-08 06:49 UTC | 40m |
| OAL2MS | OAL | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-04-08 06:26 UTC | 2026-04-08 06:49 UTC | 22m |
| N232HF |  | Teterboro Airport (KTEB) | Van Nuys Airport (KVNY) | 2026-04-08 01:37 UTC | 2026-04-08 06:44 UTC | 5h 7m |
| WIF5P | WIF | Trondheim Airport Vaernes (ENVA) | Mosjøen Airport Kjaerstad (ENMS) | 2026-04-08 06:02 UTC | 2026-04-08 06:44 UTC | 42m |
| HBZUW | HBZ | Megeve Airport (LFHM) | Sion Airport (LSGS) | 2026-04-08 06:40 UTC | 2026-04-08 06:44 UTC | 3m |
| TVS62J | TVS | Stockholm-Arlanda Airport (ESSA) | Helsinki Vantaa Airport (EFHK) | 2026-04-08 05:59 UTC | 2026-04-08 06:42 UTC | 42m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-04-08 05:28 UTC | 2026-04-08 06:41 UTC | 1h 12m |
| RYR2TY | Ryanair | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 2026-04-08 05:41 UTC | 2026-04-08 06:41 UTC | 59m |
| LUCKY21 | LUC | Kaneohe Bay Mcas (Marion E Carl Field) Airport (PHNG) | Kaneohe Bay Mcas (Marion E Carl Field) Airport (PHNG) | 2026-04-08 06:03 UTC | 2026-04-08 06:40 UTC | 36m |
| N541LM |  | Ted Stevens Anchorage International Airport (PANC) | AK04 (AK04) | 2026-04-08 06:14 UTC | 2026-04-08 06:40 UTC | 26m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-08 05:47 UTC | 2026-04-08 06:40 UTC | 52m |
| SWR4PC | Swiss International | Zurich Airport (LSZH) | Visoko Sport Airfield (LQVI) | 2026-04-08 05:35 UTC | 2026-04-08 06:39 UTC | 1h 3m |
| JST460 | JST | Sydney Kingsford Smith International Airport (YSSY) | Ballina Byron Gateway Airport (YBNA) | 2026-04-08 05:37 UTC | 2026-04-08 06:32 UTC | 55m |
| N318MT |  | Reno/Tahoe International Airport (KRNO) | Lantana Ranch Airport (01NV) | 2026-04-08 06:18 UTC | 2026-04-08 06:31 UTC | 12m |
| ANE87CJ | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-04-08 05:58 UTC | 2026-04-08 06:31 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
