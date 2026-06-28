# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_09:24:40_UTC-green)

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

**Latest saved flight:** 2026-06-28 09:24:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-28 09:24:40 UTC

- **122,233** saved flights
- **41,950** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **122,233** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,478,000.7 tonnes** estimated CO2 emissions
- **85,681,198 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5008 |
| 2 | SkyWest Airlines | 4518 |
| 3 | EJA | 2367 |
| 4 | IndiGo | 2336 |
| 5 | American Airlines | 1890 |
| 6 | Southwest Airlines | 1834 |
| 7 | ENY | 1528 |
| 8 | Delta Air Lines | 1449 |
| 9 | Lufthansa | 1322 |
| 10 | LATAM Airlines | 1092 |
| 11 | Vueling | 1090 |
| 12 | WIF | 1076 |
| 13 | AZU | 1025 |
| 14 | AXM | 985 |
| 15 | LXJ | 931 |
| 16 | Swiss International | 851 |
| 17 | All Nippon Airways | 829 |
| 18 | Alaska Airlines | 803 |
| 19 | easyJet | 786 |
| 20 | QLK | 778 |
| 21 | EJU | 766 |
| 22 | Cathay Pacific | 687 |
| 23 | AEE | 675 |
| 24 | Air France | 667 |
| 25 | VIV | 665 |
| 26 | United Airlines | 659 |
| 27 | CXK | 649 |
| 28 | MXY | 638 |
| 29 | JetBlue | 611 |
| 30 | AXB | 607 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 103878 |
| 2 | 🇪🇸 ES | 8246 |
| 3 | 🇮🇳 IN | 7341 |
| 4 | 🇦🇺 AU | 7167 |
| 5 | 🇧🇷 BR | 6749 |
| 6 | 🇩🇪 DE | 6496 |
| 7 | 🇮🇹 IT | 6495 |
| 8 | 🇨🇦 CA | 6436 |
| 9 | 🇯🇵 JP | 5409 |
| 10 | 🇬🇧 GB | 5369 |
| 11 | 🇫🇷 FR | 4845 |
| 12 | 🇨🇴 CO | 4026 |
| 13 | 🇲🇽 MX | 3561 |
| 14 | 🇬🇷 GR | 3484 |
| 15 | 🇳🇴 NO | 3358 |
| 16 | 🇨🇭 CH | 3132 |
| 17 | 🇲🇾 MY | 2551 |
| 18 | 🇹🇷 TR | 2534 |
| 19 | 🇿🇦 ZA | 2031 |
| 20 | 🇵🇱 PL | 2006 |
| 21 | 🇳🇿 NZ | 1986 |
| 22 | 🇹🇭 TH | 1931 |
| 23 | 🇰🇷 KR | 1925 |
| 24 | 🇵🇭 PH | 1752 |
| 25 | 🇬🇹 GT | 1699 |
| 26 | 🇲🇦 MA | 1311 |
| 27 | 🇲🇪 ME | 1218 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1166 |
| 30 | 🇭🇷 HR | 1054 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2568 |
| 2 | Denver International Airport |  | US | 2056 |
| 3 | Tokyo International Airport |  | JP | 1790 |
| 4 | Indira Gandhi International Airport |  | IN | 1618 |
| 5 | Harry Reid International Airport |  | US | 1527 |
| 6 | Guaymaral Airport |  | CO | 1516 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1474 |
| 8 | Zurich Airport |  | CH | 1352 |
| 9 | La Aurora Airport |  | GT | 1312 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1301 |
| 11 | Frankfurt am Main International Airport |  | DE | 1277 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1203 |
| 13 | Chicago O'Hare International Airport |  | US | 1186 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1062 |
| 17 | Capua Airport |  | IT | 1044 |
| 18 | Madrid Barajas International Airport |  | ES | 1020 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1019 |
| 20 | Kuala Lumpur International Airport |  | MY | 989 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 963 |
| 22 | Congonhas Airport |  | BR | 947 |
| 23 | Charlotte/Douglas International Airport |  | US | 923 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 904 |
| 25 | Charles de Gaulle International Airport |  | FR | 894 |
| 26 | Bengaluru International Airport |  | IN | 882 |
| 27 | Malpensa International Airport |  | IT | 850 |
| 28 | Ninoy Aquino International Airport |  | PH | 812 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 798 |
| 30 | Daniel K Inouye International Airport |  | US | 785 |
| 31 | Barcelona International Airport |  | ES | 767 |
| 32 | Tenerife Norte Airport |  | ES | 762 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 748 |
| 34 | Calgary International Airport |  | CA | 717 |
| 35 | Vitoria/Foronda Airport |  | ES | 709 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 706 |
| 37 | Amsterdam Airport Schiphol |  | NL | 704 |
| 38 | Scottsdale Airport |  | US | 704 |
| 39 | Seattle-Tacoma International Airport |  | US | 702 |
| 40 | Don Mueang International Airport |  | TH | 698 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 632 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 445 | 21m | 244 km | 1,873.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 320 | 24m | 225 km | 1,241.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 310 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 294 | 1h 10m | 770 km | 3,905.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 293 | 1h 25m | 910 km | 4,597.9 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 239 | 26m | 275 km | 1,132.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 228 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 175 | 26m | 215 km | 648.1 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 166 | 44m | 241 km | 689.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 166 | 27m | 152 km | 433.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 156 | 1h 44m | 1,423 km | 3,828.5 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 154 | 18m | 144 km | 383.1 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 142 | 1h 38m | 1,156 km | 2,832.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 139 | 1h 17m | 961 km | 2,304.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 137 | 29m | 49 km | 115.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GCPSS | GCP | Netheravon Airfield (EGDN) | Netheravon Airfield (EGDN) | 2026-06-28 08:39 UTC | 2026-06-28 09:24 UTC | 45m |
| RJA5652 | Royal Jordanian | Queen Alia International Airport (OJAI) | Hamad International Airport (OTHH) | 2026-06-28 07:00 UTC | 2026-06-28 09:20 UTC | 2h 20m |
| N105VE |  | Wels Airport (LOLW) | Wels Airport (LOLW) | 2026-06-28 08:53 UTC | 2026-06-28 09:14 UTC | 20m |
| HBSHA | HBS | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-06-28 08:27 UTC | 2026-06-28 09:10 UTC | 42m |
| OEKKV | OEK | Annemasse Airport (LFLI) | Clamecy Airport (LFJC) | 2026-06-28 08:06 UTC | 2026-06-28 09:08 UTC | 1h 2m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-06-28 01:45 UTC | 2026-06-28 09:00 UTC | 7h 14m |
| FHDSA | FHD | Vannes-Meucon Airport (LFRV) | Vannes-Meucon Airport (LFRV) | 2026-06-28 08:30 UTC | 2026-06-28 08:47 UTC | 16m |
| PHPNY | PHP | Torozos Airport (LETZ) | Valladolid Airport (LEVD) | 2026-06-28 08:27 UTC | 2026-06-28 08:40 UTC | 12m |
| RYR9GA | Ryanair | London Stansted Airport (EGSS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-06-28 06:41 UTC | 2026-06-28 08:37 UTC | 1h 56m |
| PHTWM | PHT | Twenthe Airport (EHTW) | Hoogeveen Airport (EHHO) | 2026-06-28 08:09 UTC | 2026-06-28 08:36 UTC | 26m |
| FLJ64G | FLJ | Manchester Airport (EGCC) | Manchester Airport (EGCC) | 2026-06-28 08:24 UTC | 2026-06-28 08:35 UTC | 11m |
| AUA77Z | Austrian Airlines | Vienna International Airport (LOWW) | Sofia Airport (LBSF) | 2026-06-28 07:22 UTC | 2026-06-28 08:28 UTC | 1h 6m |
| AIQ3306 | AIQ | Don Mueang International Airport (VTBD) | Nakhon Sawan Airport (VTPN) | 2026-06-28 08:05 UTC | 2026-06-28 08:26 UTC | 21m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-06-28 08:07 UTC | 2026-06-28 08:26 UTC | 19m |
| DRK541 | DRK | Changi Air Base (WSAC) | Shillong Airport (VEBI) | 2026-06-28 04:44 UTC | 2026-06-28 08:22 UTC | 3h 37m |
| DLH1100 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Santa Cilia De Jaca Airport (LECI) | 2026-06-28 06:45 UTC | 2026-06-28 08:22 UTC | 1h 36m |
| EJU4735 | EJU | Nantes Atlantique Airport (LFRS) | Chania International Airport (LGSA) | 2026-06-28 05:04 UTC | 2026-06-28 08:21 UTC | 3h 17m |
| SSZ9C | SSZ | Liverpool John Lennon Airport (EGGP) | Birmingham International Airport (EGBB) | 2026-06-28 07:59 UTC | 2026-06-28 08:20 UTC | 21m |
| RYR21AQ | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-06-28 06:47 UTC | 2026-06-28 08:19 UTC | 1h 32m |
| ANA297 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-06-28 07:33 UTC | 2026-06-28 08:19 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
