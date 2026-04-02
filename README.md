# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_08:45:57_UTC-green)

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

**Latest saved flight:** 2026-04-02 08:45:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 08:45:57 UTC

- **10,482** saved flights
- **6,144** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **10,482** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **129,597.8 tonnes** estimated CO2 emissions
- **7,512,915 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 470 |
| 2 | Ryanair | 397 |
| 3 | IndiGo | 287 |
| 4 | EJA | 215 |
| 5 | American Airlines | 188 |
| 6 | Lufthansa | 168 |
| 7 | Southwest Airlines | 164 |
| 8 | ENY | 139 |
| 9 | Vueling | 113 |
| 10 | AXM | 112 |
| 11 | LATAM Airlines | 106 |
| 12 | LXJ | 100 |
| 13 | QLK | 96 |
| 14 | All Nippon Airways | 93 |
| 15 | Delta Air Lines | 86 |
| 16 | WIF | 82 |
| 17 | Swiss International | 79 |
| 18 | Japan Airlines | 73 |
| 19 | Alaska Airlines | 72 |
| 20 | VIV | 72 |
| 21 | AZU | 71 |
| 22 | AXB | 69 |
| 23 | EDV | 66 |
| 24 | United Airlines | 66 |
| 25 | Cathay Pacific | 64 |
| 26 | Avianca | 60 |
| 27 | easyJet | 59 |
| 28 | BRC | 58 |
| 29 | EJU | 58 |
| 30 | ANZ | 56 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8545 |
| 2 | 🇦🇺 AU | 880 |
| 3 | 🇮🇳 IN | 875 |
| 4 | 🇪🇸 ES | 795 |
| 5 | 🇩🇪 DE | 553 |
| 6 | 🇯🇵 JP | 542 |
| 7 | 🇧🇷 BR | 542 |
| 8 | 🇨🇴 CO | 524 |
| 9 | 🇨🇦 CA | 512 |
| 10 | 🇮🇹 IT | 455 |
| 11 | 🇲🇽 MX | 379 |
| 12 | 🇬🇧 GB | 368 |
| 13 | 🇫🇷 FR | 315 |
| 14 | 🇳🇴 NO | 265 |
| 15 | 🇳🇿 NZ | 260 |
| 16 | 🇲🇾 MY | 251 |
| 17 | 🇬🇷 GR | 248 |
| 18 | 🇨🇭 CH | 240 |
| 19 | 🇿🇦 ZA | 211 |
| 20 | 🇬🇹 GT | 209 |
| 21 | 🇵🇭 PH | 206 |
| 22 | 🇰🇷 KR | 184 |
| 23 | 🇹🇷 TR | 166 |
| 24 | 🇮🇩 ID | 134 |
| 25 | 🇵🇱 PL | 129 |
| 26 | 🇹🇭 TH | 128 |
| 27 | 🇲🇴 MO | 124 |
| 28 | 🇲🇦 MA | 119 |
| 29 | 🇲🇪 ME | 101 |
| 30 | 🇧🇸 BS | 96 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 252 |
| 2 | Tokyo International Airport |  | JP | 195 |
| 3 | Indira Gandhi International Airport |  | IN | 194 |
| 4 | Denver International Airport |  | US | 189 |
| 5 | El Dorado International Airport |  | CO | 173 |
| 6 | Frankfurt am Main International Airport |  | DE | 171 |
| 7 | Harry Reid International Airport |  | US | 149 |
| 8 | Guaymaral Airport |  | CO | 148 |
| 9 | La Aurora Airport |  | GT | 146 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 130 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 126 |
| 12 | Macau International Airport |  | MO | 124 |
| 13 | Zurich Airport |  | CH | 121 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 118 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 106 |
| 16 | Chicago O'Hare International Airport |  | US | 105 |
| 17 | Bengaluru International Airport |  | IN | 96 |
| 18 | Reno/Tahoe International Airport |  | US | 95 |
| 19 | Madrid Barajas International Airport |  | ES | 94 |
| 20 | Kuala Lumpur International Airport |  | MY | 94 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 93 |
| 22 | Charlotte/Douglas International Airport |  | US | 92 |
| 23 | Ninoy Aquino International Airport |  | PH | 92 |
| 24 | Tenerife Norte Airport |  | ES | 92 |
| 25 | Daniel K Inouye International Airport |  | US | 81 |
| 26 | Congonhas Airport |  | BR | 81 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 80 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 80 |
| 29 | Malpensa International Airport |  | IT | 78 |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 76 |
| 31 | Salt Lake City International Airport |  | US | 75 |
| 32 | Barcelona International Airport |  | ES | 74 |
| 33 | Pune Airport |  | IN | 73 |
| 34 | Austin-Bergstrom International Airport |  | US | 72 |
| 35 | Vitoria/Foronda Airport |  | ES | 72 |
| 36 | Seattle-Tacoma International Airport |  | US | 72 |
| 37 | Charles de Gaulle International Airport |  | FR | 70 |
| 38 | Gimpo International Airport |  | KR | 68 |
| 39 | Miami International Airport |  | US | 67 |
| 40 | Calgary International Airport |  | CA | 67 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 48 | 1h 7m | 706 km | 584.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 48 | 14m | 114 km | 94.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 40 | 24m | 225 km | 155.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 35 | 29m | 304 km | 183.5 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 32 | 1h 45m | 1,156 km | 638.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 31 | 31m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 31 | 4m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 30 | 20m | 165 km | 85.3 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 30 | 23m | 99 km | 51.4 t |
| 11 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 29 | 26m | 152 km | 75.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 27 | 15m | 206 km | 96.0 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 27 | 1h 26m | 910 km | 423.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 24 | 1h 42m | 1,423 km | 589.0 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 24 | 53m | 546 km | 226.0 t |
| 18 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 23 | 28m | 275 km | 109.0 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 21 | 1h 10m | 770 km | 279.0 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 21 | 1h 58m | 1,304 km | 472.4 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 18 | 11m | 127 km | 39.4 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 17 | 23m | 252 km | 73.8 t |
| 25 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 16 | 32m | - | - |
| 28 | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 16 | 28m | 212 km | 58.5 t |
| 29 | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 16 | 18m | 26 km | 7.2 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 15 | 20m | 147 km | 38.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DLH511 | Lufthansa | Ministro Pistarini International Airport (SAEZ) | Frankfurt am Main International Airport (EDDF) | 2026-04-01 20:06 UTC | 2026-04-02 08:45 UTC | 12h 39m |
| R21202 |  | Ladd Army Air Field (PAFB) | Manley Hot Springs Airport (PAML) | 2026-04-02 07:36 UTC | 2026-04-02 08:37 UTC | 1h 0m |
| FKH8012 | FKH | Riga International Airport (EVRA) | Macau International Airport (VMMC) | 2026-04-01 18:54 UTC | 2026-04-02 08:33 UTC | 13h 38m |
| LSI137 | LSI | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-01 21:30 UTC | 2026-04-02 08:27 UTC | 10h 57m |
| ARK401A | ARK | Sabadell Airport (LELL) | Girona Airport (LEGE) | 2026-04-02 07:46 UTC | 2026-04-02 08:18 UTC | 31m |
| CJT570 | CJT | Winnipeg James Armstrong Richardson International Airport (CYWG) | Montréal (Mirabel) Airport (CYMX) | 2026-04-02 06:12 UTC | 2026-04-02 08:14 UTC | 2h 2m |
| THY70 | Turkish Airlines | Eleftherios Venizelos International Airport (LGAV) | Macau International Airport (VMMC) | 2026-04-01 19:34 UTC | 2026-04-02 08:12 UTC | 12h 37m |
| EZY86ZC | easyJet | London Gatwick Airport (EGKK) | Tivat Airport (LYTV) | 2026-04-02 05:52 UTC | 2026-04-02 08:09 UTC | 2h 17m |
| BTK7366 | BTK | Soekarno-Hatta International Airport (WIII) | Adi Sumarmo Wiryokusumo Airport (WARQ) | 2026-04-02 07:02 UTC | 2026-04-02 08:07 UTC | 1h 5m |
| GIA228 | Garuda Indonesia | Soekarno-Hatta International Airport (WIII) | Adi Sumarmo Wiryokusumo Airport (WARQ) | 2026-04-02 07:09 UTC | 2026-04-02 08:02 UTC | 52m |
| OEBXS | OEB | Kapfenberg Airport (LOGK) | Kapfenberg Airport (LOGK) | 2026-04-02 08:01 UTC | 2026-04-02 08:01 UTC | 0m |
| ROF9143 | ROF | Henri Coanda International Airport (LROP) | LRCD (LRCD) | 2026-04-02 07:33 UTC | 2026-04-02 08:00 UTC | 27m |
| IGO6537 | IndiGo | Bengaluru International Airport (VOBL) | Giridih Airport (VE41) | 2026-04-02 06:09 UTC | 2026-04-02 07:57 UTC | 1h 48m |
| AEA17AZ | AEA | Madrid Barajas International Airport (LEMD) | Frankfurt am Main International Airport (EDDF) | 2026-04-02 05:49 UTC | 2026-04-02 07:56 UTC | 2h 7m |
| IGO6535 | IndiGo | Bengaluru International Airport (VOBL) | Biju Patnaik Airport (VEBS) | 2026-04-02 06:37 UTC | 2026-04-02 07:56 UTC | 1h 18m |
| 2612 |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-02 07:39 UTC | 2026-04-02 07:53 UTC | 14m |
| RYR68NZ | Ryanair | Niederrhein Airport (EDLV) | Ampuriabrava Airport (LEAP) | 2026-04-02 06:23 UTC | 2026-04-02 07:52 UTC | 1h 28m |
| SWR1DL | Swiss International | Zurich Airport (LSZH) | Malpensa International Airport (LIMC) | 2026-04-02 07:06 UTC | 2026-04-02 07:49 UTC | 43m |
| AXM6037 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-02 07:29 UTC | 2026-04-02 07:48 UTC | 19m |
| VLG8484 | Vueling | Barcelona International Airport (LEBL) | Faro Airport (LPFR) | 2026-04-02 06:21 UTC | 2026-04-02 07:48 UTC | 1h 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
