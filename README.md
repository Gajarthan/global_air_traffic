# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_02:58:07_UTC-green)

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

**Latest saved flight:** 2026-04-05 02:58:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 02:58:07 UTC

- **17,204** saved flights
- **9,007** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **17,204** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **215,092.5 tonnes** estimated CO2 emissions
- **12,469,132 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 768 |
| 2 | Ryanair | 689 |
| 3 | IndiGo | 487 |
| 4 | EJA | 328 |
| 5 | American Airlines | 319 |
| 6 | Southwest Airlines | 245 |
| 7 | Lufthansa | 238 |
| 8 | ENY | 234 |
| 9 | Vueling | 189 |
| 10 | LATAM Airlines | 184 |
| 11 | AXM | 163 |
| 12 | Delta Air Lines | 150 |
| 13 | LXJ | 149 |
| 14 | All Nippon Airways | 142 |
| 15 | QLK | 140 |
| 16 | VIV | 131 |
| 17 | AZU | 130 |
| 18 | Swiss International | 124 |
| 19 | Alaska Airlines | 119 |
| 20 | United Airlines | 116 |
| 21 | Avianca | 113 |
| 22 | EJU | 109 |
| 23 | Japan Airlines | 109 |
| 24 | EDV | 108 |
| 25 | easyJet | 107 |
| 26 | AEE | 105 |
| 27 | AXB | 105 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | GLO | 99 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13830 |
| 2 | 🇮🇳 IN | 1487 |
| 3 | 🇪🇸 ES | 1400 |
| 4 | 🇦🇺 AU | 1228 |
| 5 | 🇧🇷 BR | 998 |
| 6 | 🇨🇴 CO | 903 |
| 7 | 🇯🇵 JP | 881 |
| 8 | 🇩🇪 DE | 874 |
| 9 | 🇮🇹 IT | 788 |
| 10 | 🇨🇦 CA | 774 |
| 11 | 🇬🇧 GB | 661 |
| 12 | 🇫🇷 FR | 610 |
| 13 | 🇲🇽 MX | 600 |
| 14 | 🇬🇷 GR | 461 |
| 15 | 🇨🇭 CH | 445 |
| 16 | 🇳🇿 NZ | 388 |
| 17 | 🇲🇾 MY | 375 |
| 18 | 🇿🇦 ZA | 350 |
| 19 | 🇳🇴 NO | 341 |
| 20 | 🇬🇹 GT | 335 |
| 21 | 🇵🇭 PH | 325 |
| 22 | 🇹🇷 TR | 310 |
| 23 | 🇰🇷 KR | 294 |
| 24 | 🇵🇱 PL | 239 |
| 25 | 🇹🇭 TH | 232 |
| 26 | 🇲🇦 MA | 210 |
| 27 | 🇧🇸 BS | 191 |
| 28 | 🇮🇩 ID | 182 |
| 29 | 🇲🇴 MO | 176 |
| 30 | 🇲🇪 ME | 173 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 417 |
| 2 | El Dorado International Airport |  | CO | 342 |
| 3 | Denver International Airport |  | US | 325 |
| 4 | Indira Gandhi International Airport |  | IN | 307 |
| 5 | Tokyo International Airport |  | JP | 303 |
| 6 | La Aurora Airport |  | GT | 236 |
| 7 | Harry Reid International Airport |  | US | 230 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 215 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 204 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 188 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 182 |
| 13 | Guaymaral Airport |  | CO | 182 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 15 | Macau International Airport |  | MO | 176 |
| 16 | Chicago O'Hare International Airport |  | US | 172 |
| 17 | Bengaluru International Airport |  | IN | 165 |
| 18 | Charlotte/Douglas International Airport |  | US | 163 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 156 |
| 20 | Madrid Barajas International Airport |  | ES | 156 |
| 21 | Congonhas Airport |  | BR | 154 |
| 22 | Tenerife Norte Airport |  | ES | 150 |
| 23 | Ninoy Aquino International Airport |  | PH | 149 |
| 24 | Salt Lake City International Airport |  | US | 141 |
| 25 | Daniel K Inouye International Airport |  | US | 138 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 137 |
| 27 | Reno/Tahoe International Airport |  | US | 135 |
| 28 | Kuala Lumpur International Airport |  | MY | 134 |
| 29 | Malpensa International Airport |  | IT | 133 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 129 |
| 31 | Vitoria/Foronda Airport |  | ES | 125 |
| 32 | Charles de Gaulle International Airport |  | FR | 124 |
| 33 | Miami International Airport |  | US | 122 |
| 34 | Barcelona International Airport |  | ES | 120 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 36 | Pune Airport |  | IN | 116 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 111 |
| 38 | Seattle-Tacoma International Airport |  | US | 111 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 79 | 14m | 114 km | 154.9 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 75 | 1h 8m | 706 km | 913.1 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 69 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 62 | 24m | 225 km | 240.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 53 | 27m | 152 km | 138.5 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 50 | 31m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 45 | 16m | 206 km | 160.0 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 45 | 22m | 99 km | 77.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 40 | 28m | 275 km | 189.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 38 | 19m | 165 km | 108.1 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 38 | 1h 54m | 1,304 km | 854.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 37 | 30m | 369 km | 235.5 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 17 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 35 | 1h 11m | 770 km | 464.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 32 | 1h 43m | 1,423 km | 785.3 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 31 | 58m | 723 km | 386.5 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 29 | 11m | 127 km | 63.5 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 28 | 46m | 452 km | 218.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CCA101 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-04-05 00:17 UTC | 2026-04-05 02:58 UTC | 2h 40m |
| N52908 |  | Fort Worth Meacham International Airport (KFTW) | Cisco Municipal Airport (K3F2) | 2026-04-05 02:08 UTC | 2026-04-05 02:54 UTC | 45m |
| SRQ6129 | SRQ | Diosdado Macapagal International Airport (RPLC) | Bulan Airport (RPUU) | 2026-04-05 01:43 UTC | 2026-04-05 02:27 UTC | 43m |
| AXM6042 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-05 02:04 UTC | 2026-04-05 02:23 UTC | 19m |
| N149AH |  | Peter O Knight Airport (KTPF) | Orlando Executive Airport (KORL) | 2026-04-05 01:37 UTC | 2026-04-05 02:20 UTC | 43m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-04-05 01:58 UTC | 2026-04-05 02:18 UTC | 20m |
| UBG141 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-05 01:39 UTC | 2026-04-05 02:14 UTC | 34m |
| FFT4103 | FFT | Harry Reid International Airport (KLAS) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-05 01:11 UTC | 2026-04-05 02:13 UTC | 1h 1m |
| STT224 | STT | Daniel K Inouye International Airport (PHNL) | Kaluakoi Airport (HI49) | 2026-04-05 02:04 UTC | 2026-04-05 02:13 UTC | 9m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-04-05 01:45 UTC | 2026-04-05 02:12 UTC | 27m |
| IGO493H | IndiGo | Juhu Aerodrome (VAJJ) | VEDG (VEDG) | 2026-04-05 00:25 UTC | 2026-04-05 02:12 UTC | 1h 47m |
| UBG183 | UBG | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-04-05 01:34 UTC | 2026-04-05 02:11 UTC | 36m |
| N395CF |  | John Wayne/Orange County Airport (KSNA) | Borrego Air Ranch Airport (58CL) | 2026-04-05 01:45 UTC | 2026-04-05 02:08 UTC | 23m |
| ANZ309L | ANZ | Wellington International Airport (NZWN) | Picton Aerodrome (NZPN) | 2026-04-05 01:56 UTC | 2026-04-05 02:06 UTC | 10m |
| MAS1051 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-05 01:49 UTC | 2026-04-05 02:05 UTC | 15m |
| IGO5EP | IndiGo | Indira Gandhi International Airport (VIDP) | Chandigarh Airport (VICG) | 2026-04-05 01:28 UTC | 2026-04-05 02:04 UTC | 35m |
| JAL663 | Japan Airlines | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-05 00:50 UTC | 2026-04-05 02:02 UTC | 1h 12m |
| IGO697L | IndiGo | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-04-05 01:41 UTC | 2026-04-05 02:02 UTC | 20m |
| FDA142 | FDA | Fukuoka Airport (RJFF) | Hamamatsu Airport (RJNH) | 2026-04-05 01:10 UTC | 2026-04-05 02:01 UTC | 51m |
| VIV7435 | VIV | General Heriberto Jara International Airport (MMVR) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-05 01:19 UTC | 2026-04-05 02:00 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
