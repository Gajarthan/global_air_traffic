# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_17:33:00_UTC-green)

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

**Latest saved flight:** 2026-06-14 17:33:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 17:33:00 UTC

- **110,308** saved flights
- **38,483** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **110,308** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,348,317.0 tonnes** estimated CO2 emissions
- **78,163,302 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4557 |
| 2 | SkyWest Airlines | 4118 |
| 3 | IndiGo | 2173 |
| 4 | EJA | 2123 |
| 5 | American Airlines | 1736 |
| 6 | Southwest Airlines | 1653 |
| 7 | ENY | 1369 |
| 8 | Delta Air Lines | 1299 |
| 9 | Lufthansa | 1253 |
| 10 | Vueling | 1012 |
| 11 | LATAM Airlines | 973 |
| 12 | WIF | 973 |
| 13 | AXM | 933 |
| 14 | AZU | 909 |
| 15 | LXJ | 836 |
| 16 | Swiss International | 795 |
| 17 | All Nippon Airways | 769 |
| 18 | Alaska Airlines | 750 |
| 19 | QLK | 726 |
| 20 | easyJet | 709 |
| 21 | EJU | 703 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 624 |
| 24 | VIV | 621 |
| 25 | Air France | 618 |
| 26 | United Airlines | 607 |
| 27 | MXY | 588 |
| 28 | CXK | 578 |
| 29 | AXB | 545 |
| 30 | Japan Airlines | 542 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 92676 |
| 2 | 🇪🇸 ES | 7584 |
| 3 | 🇮🇳 IN | 6850 |
| 4 | 🇦🇺 AU | 6567 |
| 5 | 🇧🇷 BR | 6073 |
| 6 | 🇮🇹 IT | 5944 |
| 7 | 🇩🇪 DE | 5917 |
| 8 | 🇨🇦 CA | 5768 |
| 9 | 🇯🇵 JP | 5015 |
| 10 | 🇬🇧 GB | 4724 |
| 11 | 🇫🇷 FR | 4423 |
| 12 | 🇨🇴 CO | 3761 |
| 13 | 🇲🇽 MX | 3272 |
| 14 | 🇬🇷 GR | 3146 |
| 15 | 🇳🇴 NO | 3057 |
| 16 | 🇨🇭 CH | 2831 |
| 17 | 🇲🇾 MY | 2409 |
| 18 | 🇹🇷 TR | 2176 |
| 19 | 🇿🇦 ZA | 1887 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1826 |
| 22 | 🇵🇱 PL | 1816 |
| 23 | 🇳🇿 NZ | 1807 |
| 24 | 🇵🇭 PH | 1611 |
| 25 | 🇬🇹 GT | 1574 |
| 26 | 🇲🇦 MA | 1216 |
| 27 | 🇲🇴 MO | 1149 |
| 28 | 🇳🇱 NL | 1083 |
| 29 | 🇲🇪 ME | 1077 |
| 30 | 🇭🇷 HR | 961 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2356 |
| 2 | Denver International Airport |  | US | 1862 |
| 3 | Tokyo International Airport |  | JP | 1661 |
| 4 | Indira Gandhi International Airport |  | IN | 1490 |
| 5 | Guaymaral Airport |  | CO | 1395 |
| 6 | Harry Reid International Airport |  | US | 1392 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1377 |
| 8 | Zurich Airport |  | CH | 1244 |
| 9 | Frankfurt am Main International Airport |  | DE | 1228 |
| 10 | La Aurora Airport |  | GT | 1211 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1178 |
| 12 | Macau International Airport |  | MO | 1149 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1098 |
| 15 | Chicago O'Hare International Airport |  | US | 1089 |
| 16 | Madrid Barajas International Airport |  | ES | 966 |
| 17 | Capua Airport |  | IT | 954 |
| 18 | Kuala Lumpur International Airport |  | MY | 940 |
| 19 | Salt Lake City International Airport |  | US | 931 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 931 |
| 21 | Charlotte/Douglas International Airport |  | US | 847 |
| 22 | Congonhas Airport |  | BR | 843 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Charles de Gaulle International Airport |  | FR | 828 |
| 25 | Bengaluru International Airport |  | IN | 828 |
| 26 | Malpensa International Airport |  | IT | 805 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 745 |
| 28 | Ninoy Aquino International Airport |  | PH | 742 |
| 29 | Daniel K Inouye International Airport |  | US | 735 |
| 30 | Tenerife Norte Airport |  | ES | 730 |
| 31 | Barcelona International Airport |  | ES | 722 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 716 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 703 |
| 34 | Don Mueang International Airport |  | TH | 667 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 655 |
| 37 | Calgary International Airport |  | CA | 649 |
| 38 | Seattle-Tacoma International Airport |  | US | 631 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 630 |
| 40 | Viracopos International Airport |  | BR | 621 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 578 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 403 | 21m | 244 km | 1,696.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 285 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 271 | 1h 25m | 910 km | 4,252.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 260 | 1h 10m | 770 km | 3,453.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 220 | 26m | 275 km | 1,042.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 163 | 20m | 99 km | 279.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 160 | 27m | 215 km | 592.6 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 156 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 145 | 18m | 144 km | 360.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 138 | 44m | 241 km | 573.2 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 123 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 122 | 24m | 223 km | 469.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N32296 |  | Rock Hill/York County/Bryant Field (KUZA) | Rock Hill/York County/Bryant Field (KUZA) | 2026-06-14 17:18 UTC | 2026-06-14 17:33 UTC | 14m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-14 15:49 UTC | 2026-06-14 17:31 UTC | 1h 42m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-06-14 16:00 UTC | 2026-06-14 17:31 UTC | 1h 30m |
| BRG661 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-06-14 16:56 UTC | 2026-06-14 17:26 UTC | 29m |
| CAP2688 | CAP | Fremont Municipal Airport (KFET) | Scribner State Airport (KSCB) | 2026-06-14 16:57 UTC | 2026-06-14 17:21 UTC | 23m |
| N129LA |  | K1J0 (K1J0) | K1J0 (K1J0) | 2026-06-14 17:09 UTC | 2026-06-14 17:21 UTC | 12m |
| N495KL |  | Moton Field Municipal Airport (K06A) | Moton Field Municipal Airport (K06A) | 2026-06-14 17:01 UTC | 2026-06-14 17:18 UTC | 16m |
| N739PG |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-06-14 17:00 UTC | 2026-06-14 17:13 UTC | 12m |
| FHCHF | FHC | Le Mans-Arnage Airport (LFRM) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-06-14 16:30 UTC | 2026-06-14 17:12 UTC | 41m |
| N646CB |  | Chino Airport (KCNO) | San Gabriel Valley Airport (KEMT) | 2026-06-14 16:57 UTC | 2026-06-14 17:11 UTC | 14m |
| LXJ323 | LXJ | Paso Robles Municipal Airport (KPRB) | Buchanan Field (KCCR) | 2026-06-14 16:33 UTC | 2026-06-14 17:08 UTC | 35m |
| N1086U |  | Stennis International Airport (KHSA) | Stennis International Airport (KHSA) | 2026-06-14 16:26 UTC | 2026-06-14 17:06 UTC | 40m |
| N445B |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-06-14 17:06 UTC | 2026-06-14 17:06 UTC | 0m |
| N97FN |  | Charles M Schulz/Sonoma County Airport (KSTS) | Truckee-Tahoe Airport (KTRK) | 2026-06-14 16:29 UTC | 2026-06-14 17:00 UTC | 31m |
| N140PJ |  | Pueblo Memorial Airport (KPUB) | Usaf Academy Davis Airfield (KAFF) | 2026-06-14 16:24 UTC | 2026-06-14 16:59 UTC | 34m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-06-14 16:47 UTC | 2026-06-14 16:58 UTC | 10m |
| TGFSS | TGF | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-06-14 16:52 UTC | 2026-06-14 16:57 UTC | 4m |
| N937SA |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-06-14 16:55 UTC | 2026-06-14 16:57 UTC | 1m |
| JBU892 | JetBlue | Tampa International Airport (KTPA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-14 14:20 UTC | 2026-06-14 16:57 UTC | 2h 36m |
| N7403 |  | Gerald R Ford International Airport (KGRR) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-14 15:23 UTC | 2026-06-14 16:55 UTC | 1h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
