# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_09:38:10_UTC-green)

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

**Latest saved flight:** 2026-04-08 09:38:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 09:38:10 UTC

- **22,989** saved flights
- **11,225** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,989** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **285,055.5 tonnes** estimated CO2 emissions
- **16,524,958 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 971 |
| 2 | Ryanair | 947 |
| 3 | IndiGo | 646 |
| 4 | EJA | 422 |
| 5 | American Airlines | 420 |
| 6 | Southwest Airlines | 330 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 290 |
| 9 | Vueling | 239 |
| 10 | AXM | 234 |
| 11 | LATAM Airlines | 230 |
| 12 | All Nippon Airways | 213 |
| 13 | QLK | 213 |
| 14 | Delta Air Lines | 200 |
| 15 | LXJ | 189 |
| 16 | AZU | 182 |
| 17 | Swiss International | 168 |
| 18 | VIV | 162 |
| 19 | Japan Airlines | 160 |
| 20 | Alaska Airlines | 158 |
| 21 | easyJet | 154 |
| 22 | EJU | 150 |
| 23 | United Airlines | 147 |
| 24 | AEE | 144 |
| 25 | WIF | 140 |
| 26 | Avianca | 139 |
| 27 | EDV | 135 |
| 28 | AXB | 129 |
| 29 | Air France | 121 |
| 30 | ANZ | 118 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18016 |
| 2 | 🇮🇳 IN | 1955 |
| 3 | 🇪🇸 ES | 1771 |
| 4 | 🇦🇺 AU | 1726 |
| 5 | 🇯🇵 JP | 1318 |
| 6 | 🇧🇷 BR | 1287 |
| 7 | 🇨🇴 CO | 1181 |
| 8 | 🇮🇹 IT | 1163 |
| 9 | 🇩🇪 DE | 1149 |
| 10 | 🇨🇦 CA | 1029 |
| 11 | 🇬🇧 GB | 909 |
| 12 | 🇫🇷 FR | 843 |
| 13 | 🇲🇽 MX | 747 |
| 14 | 🇬🇷 GR | 658 |
| 15 | 🇨🇭 CH | 629 |
| 16 | 🇲🇾 MY | 549 |
| 17 | 🇿🇦 ZA | 498 |
| 18 | 🇳🇿 NZ | 497 |
| 19 | 🇳🇴 NO | 484 |
| 20 | 🇬🇹 GT | 467 |
| 21 | 🇵🇭 PH | 442 |
| 22 | 🇹🇷 TR | 437 |
| 23 | 🇰🇷 KR | 415 |
| 24 | 🇹🇭 TH | 366 |
| 25 | 🇵🇱 PL | 330 |
| 26 | 🇲🇦 MA | 277 |
| 27 | 🇧🇸 BS | 243 |
| 28 | 🇮🇩 ID | 242 |
| 29 | 🇲🇪 ME | 234 |
| 30 | 🇳🇱 NL | 226 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 550 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 440 |
| 4 | Denver International Airport |  | US | 407 |
| 5 | Indira Gandhi International Airport |  | IN | 394 |
| 6 | La Aurora Airport |  | GT | 322 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 317 |
| 8 | Harry Reid International Airport |  | US | 308 |
| 9 | Zurich Airport |  | CH | 278 |
| 10 | Frankfurt am Main International Airport |  | DE | 254 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 240 |
| 14 | Chicago O'Hare International Airport |  | US | 238 |
| 15 | Guaymaral Airport |  | CO | 236 |
| 16 | Bengaluru International Airport |  | IN | 222 |
| 17 | Macau International Airport |  | MO | 221 |
| 18 | Charlotte/Douglas International Airport |  | US | 214 |
| 19 | Madrid Barajas International Airport |  | ES | 205 |
| 20 | Ninoy Aquino International Airport |  | PH | 203 |
| 21 | Tenerife Norte Airport |  | ES | 202 |
| 22 | Kuala Lumpur International Airport |  | MY | 198 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 24 | Congonhas Airport |  | BR | 186 |
| 25 | Malpensa International Airport |  | IT | 184 |
| 26 | Salt Lake City International Airport |  | US | 182 |
| 27 | Daniel K Inouye International Airport |  | US | 177 |
| 28 | Reno/Tahoe International Airport |  | US | 175 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 30 | Charles de Gaulle International Airport |  | FR | 169 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 156 |
| 33 | O. R. Tambo International Airport |  | ZA | 154 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 152 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 152 |
| 36 | Pune Airport |  | IN | 152 |
| 37 | Seattle-Tacoma International Airport |  | US | 150 |
| 38 | Vitoria/Foronda Airport |  | ES | 150 |
| 39 | Barcelona International Airport |  | ES | 147 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 112 | 1h 8m | 706 km | 1,363.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 87 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 82 | 28m | 304 km | 429.9 t |
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
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 43 | 20m | 250 km | 185.7 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 42 | 46m | 452 km | 327.3 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 39 | 1h 43m | 1,423 km | 957.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 33 | 20m | 147 km | 83.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZVU | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-04-08 09:27 UTC | 2026-04-08 09:38 UTC | 11m |
| GAF420 | GAF | Wunstorf Airport (ETNW) | Nuremberg Airport (EDDN) | 2026-04-08 08:54 UTC | 2026-04-08 09:33 UTC | 38m |
| GLO1495 | GLO | Frutal Airport (SNFU) | Garca Airport (SDGC) | 2026-04-08 08:54 UTC | 2026-04-08 09:28 UTC | 34m |
| MRL37F | MRL | San Javier Airport (LELC) | Alhama De Murcia Airport (LELH) | 2026-04-08 08:52 UTC | 2026-04-08 09:27 UTC | 35m |
| GCBZH | GCB | Caernarfon Airport (EGCK) | Caernarfon Airport (EGCK) | 2026-04-08 09:05 UTC | 2026-04-08 09:25 UTC | 20m |
| NOZ52K | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-04-08 08:43 UTC | 2026-04-08 09:23 UTC | 39m |
| QLK1529 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-04-08 08:08 UTC | 2026-04-08 09:11 UTC | 1h 2m |
| HBZUR | HBZ | Wangen-Lachen Airport (LSPV) | LSMF (LSMF) | 2026-04-08 08:33 UTC | 2026-04-08 09:10 UTC | 37m |
| BB25 |  | Herning Airport (EKHG) | Herning Airport (EKHG) | 2026-04-08 08:54 UTC | 2026-04-08 09:09 UTC | 14m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-07 22:06 UTC | 2026-04-08 09:07 UTC | 11h 1m |
| RYR712F | Ryanair | Bristol International Airport (EGGD) | Oksywie Military Air Base (EPOK) | 2026-04-08 07:12 UTC | 2026-04-08 09:06 UTC | 1h 53m |
| EZY527C | easyJet | Newcastle Airport (EGNT) | Bristol International Airport (EGGD) | 2026-04-08 08:13 UTC | 2026-04-08 09:00 UTC | 46m |
| SWR2GE | Swiss International | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-04-08 08:06 UTC | 2026-04-08 08:56 UTC | 50m |
| CLX4162 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-04-07 22:01 UTC | 2026-04-08 08:52 UTC | 10h 51m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-04-08 08:27 UTC | 2026-04-08 08:50 UTC | 23m |
| GCKYL | GCK | Compton Abbas Aerodrome (EGHA) | Compton Abbas Aerodrome (EGHA) | 2026-04-08 08:43 UTC | 2026-04-08 08:49 UTC | 6m |
| KUR | KUR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-08 08:14 UTC | 2026-04-08 08:48 UTC | 34m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-08 01:40 UTC | 2026-04-08 08:46 UTC | 7h 6m |
| OEXTE | OEX | LIVD (LIVD) | LIVD (LIVD) | 2026-04-08 08:35 UTC | 2026-04-08 08:45 UTC | 10m |
| CSI502 | CSI | Albuquerque International Sunport Airport (KABQ) | Crownpoint Airport (K0E8) | 2026-04-08 08:20 UTC | 2026-04-08 08:45 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
