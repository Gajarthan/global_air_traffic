# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_09:34:47_UTC-green)

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

**Latest saved flight:** 2026-06-19 09:34:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-19 09:34:47 UTC

- **114,317** saved flights
- **39,648** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **114,317** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,392,667.5 tonnes** estimated CO2 emissions
- **80,734,347 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4714 |
| 2 | SkyWest Airlines | 4260 |
| 3 | EJA | 2211 |
| 4 | IndiGo | 2211 |
| 5 | American Airlines | 1797 |
| 6 | Southwest Airlines | 1696 |
| 7 | ENY | 1421 |
| 8 | Delta Air Lines | 1347 |
| 9 | Lufthansa | 1276 |
| 10 | Vueling | 1037 |
| 11 | WIF | 1016 |
| 12 | LATAM Airlines | 1009 |
| 13 | AZU | 958 |
| 14 | AXM | 950 |
| 15 | LXJ | 869 |
| 16 | Swiss International | 811 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 771 |
| 19 | QLK | 748 |
| 20 | easyJet | 733 |
| 21 | EJU | 717 |
| 22 | Cathay Pacific | 671 |
| 23 | AEE | 644 |
| 24 | VIV | 633 |
| 25 | United Airlines | 632 |
| 26 | Air France | 631 |
| 27 | CXK | 605 |
| 28 | MXY | 605 |
| 29 | AXB | 562 |
| 30 | GLO | 558 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 96335 |
| 2 | 🇪🇸 ES | 7808 |
| 3 | 🇮🇳 IN | 6982 |
| 4 | 🇦🇺 AU | 6815 |
| 5 | 🇧🇷 BR | 6319 |
| 6 | 🇮🇹 IT | 6131 |
| 7 | 🇩🇪 DE | 6113 |
| 8 | 🇨🇦 CA | 5988 |
| 9 | 🇯🇵 JP | 5158 |
| 10 | 🇬🇧 GB | 4940 |
| 11 | 🇫🇷 FR | 4550 |
| 12 | 🇨🇴 CO | 3910 |
| 13 | 🇲🇽 MX | 3373 |
| 14 | 🇬🇷 GR | 3265 |
| 15 | 🇳🇴 NO | 3159 |
| 16 | 🇨🇭 CH | 2918 |
| 17 | 🇲🇾 MY | 2458 |
| 18 | 🇹🇷 TR | 2304 |
| 19 | 🇿🇦 ZA | 1935 |
| 20 | 🇳🇿 NZ | 1888 |
| 21 | 🇰🇷 KR | 1878 |
| 22 | 🇹🇭 TH | 1869 |
| 23 | 🇵🇱 PL | 1868 |
| 24 | 🇵🇭 PH | 1667 |
| 25 | 🇬🇹 GT | 1627 |
| 26 | 🇲🇦 MA | 1249 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1126 |
| 29 | 🇳🇱 NL | 1107 |
| 30 | 🇭🇷 HR | 996 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2426 |
| 2 | Denver International Airport |  | US | 1938 |
| 3 | Tokyo International Airport |  | JP | 1712 |
| 4 | Indira Gandhi International Airport |  | IN | 1524 |
| 5 | Guaymaral Airport |  | CO | 1445 |
| 6 | Harry Reid International Airport |  | US | 1437 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1409 |
| 8 | Zurich Airport |  | CH | 1280 |
| 9 | La Aurora Airport |  | GT | 1255 |
| 10 | Frankfurt am Main International Airport |  | DE | 1245 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1225 |
| 12 | Macau International Airport |  | MO | 1168 |
| 13 | El Dorado International Airport |  | CO | 1159 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1140 |
| 15 | Chicago O'Hare International Airport |  | US | 1127 |
| 16 | Capua Airport |  | IT | 994 |
| 17 | Madrid Barajas International Airport |  | ES | 981 |
| 18 | Salt Lake City International Airport |  | US | 969 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 959 |
| 20 | Kuala Lumpur International Airport |  | MY | 952 |
| 21 | Charlotte/Douglas International Airport |  | US | 883 |
| 22 | Congonhas Airport |  | BR | 875 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 856 |
| 24 | Bengaluru International Airport |  | IN | 847 |
| 25 | Charles de Gaulle International Airport |  | FR | 844 |
| 26 | Malpensa International Airport |  | IT | 822 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 820 |
| 28 | Ninoy Aquino International Airport |  | PH | 768 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 752 |
| 30 | Daniel K Inouye International Airport |  | US | 747 |
| 31 | Tenerife Norte Airport |  | ES | 744 |
| 32 | Barcelona International Airport |  | ES | 735 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 720 |
| 34 | Don Mueang International Airport |  | TH | 678 |
| 35 | Vitoria/Foronda Airport |  | ES | 676 |
| 36 | Amsterdam Airport Schiphol |  | NL | 674 |
| 37 | Calgary International Airport |  | CA | 671 |
| 38 | Seattle-Tacoma International Airport |  | US | 661 |
| 39 | Viracopos International Airport |  | BR | 655 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 653 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 600 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 413 | 21m | 244 km | 1,739.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 306 | 24m | 225 km | 1,187.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 297 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 282 | 1h 25m | 910 km | 4,425.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 278 | 14m | 114 km | 545.2 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 274 | 1h 10m | 770 km | 3,639.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 228 | 26m | 275 km | 1,080.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 212 | 31m | - | - |
| 13 | Bodø Airport (ENBO) | ENEN (ENEN) | 168 | 13m | - | - |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 168 | 22m | 55 km | 159.7 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 155 | 27m | 152 km | 405.1 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 148 | 44m | 241 km | 614.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 145 | 20m | 250 km | 626.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 137 | 1h 1m | 695 km | 1,642.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 134 | 1h 43m | 1,423 km | 3,288.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 130 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 129 | 1h 17m | 961 km | 2,138.2 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 127 | 12m | 99 km | 217.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AEE4319 | AEE | Kuopio Airport (EFKU) | Seduva Airport (EYSE) | 2026-06-19 08:35 UTC | 2026-06-19 09:34 UTC | 59m |
| GCDMX | GCD | Gloucestershire Airport (EGBJ) | Gloucestershire Airport (EGBJ) | 2026-06-19 09:08 UTC | 2026-06-19 09:24 UTC | 15m |
| BTK7041 | BTK | Soekarno-Hatta International Airport (WIII) | Adi Sumarmo Wiryokusumo Airport (WARQ) | 2026-06-19 08:40 UTC | 2026-06-19 09:23 UTC | 42m |
| WIF8122 | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-06-19 08:59 UTC | 2026-06-19 09:14 UTC | 15m |
| ANE42SD | ANE | Almeria International Airport (LEAM) | Melilla Airport (GEML) | 2026-06-19 08:47 UTC | 2026-06-19 09:13 UTC | 26m |
| LR5184 |  | Coffs Harbour Airport (YSCH) | Wollomombi Airport (YWMM) | 2026-06-19 08:52 UTC | 2026-06-19 09:11 UTC | 18m |
| AIB56LR | AIB | Toulouse-Blagnac Airport (LFBO) | Perpignan-Rivesaltes (Llabanere) Airport (LFMP) | 2026-06-19 08:33 UTC | 2026-06-19 09:10 UTC | 36m |
| SPGMS | SPG | Katowice International Airport (EPKT) | Dubrovnik Airport (LDDU) | 2026-06-19 07:54 UTC | 2026-06-19 09:08 UTC | 1h 14m |
| SHA123 | SHA | Tribhuvan International Airport (VNKT) | Tulsipur Airport (VNDG) | 2026-06-19 08:28 UTC | 2026-06-19 09:02 UTC | 34m |
| SBI2626 | SBI | Spichenkovo Airport (UNWW) | Kasimovo Airfield (XLLN) | 2026-06-19 01:55 UTC | 2026-06-19 09:00 UTC | 7h 5m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-06-19 08:48 UTC | 2026-06-19 09:00 UTC | 12m |
| EFC22T | EFC | OM11 (OM11) | Al Maktoum International Airport (OMDW) | 2026-06-19 08:01 UTC | 2026-06-19 08:59 UTC | 58m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Muenster Aero Airport (LSPU) | 2026-06-19 08:52 UTC | 2026-06-19 08:59 UTC | 6m |
| VOE3598 | VOE | Jayena Airport (LE84) | Vitoria/Foronda Airport (LEVT) | 2026-06-19 08:01 UTC | 2026-06-19 08:54 UTC | 53m |
| NJE918Y | NJE | Mollis Airport (LSZM) | Perugia / San Egidio Airport (LIRZ) | 2026-06-19 07:46 UTC | 2026-06-19 08:52 UTC | 1h 6m |
| SXAEN | SXA | Amigdhaleon Airport (LGKM) | Sedes Airport (LGSD) | 2026-06-19 07:50 UTC | 2026-06-19 08:51 UTC | 1h 0m |
| RYR93SK | Ryanair | Ireland West Knock Airport (EIKN) | Birmingham International Airport (EGBB) | 2026-06-19 08:00 UTC | 2026-06-19 08:50 UTC | 50m |
| DMNVA | DMN | Porta Westfalica Airport (EDVY) | Porta Westfalica Airport (EDVY) | 2026-06-19 08:48 UTC | 2026-06-19 08:50 UTC | 1m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Stykkishólmur Airport (BIST) | 2026-06-19 08:31 UTC | 2026-06-19 08:49 UTC | 17m |
| RXA2131 | RXA | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-06-19 07:57 UTC | 2026-06-19 08:45 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
