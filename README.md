# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_22:42:06_UTC-green)

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

**Latest saved flight:** 2026-06-14 22:42:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 22:42:06 UTC

- **110,959** saved flights
- **38,705** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **110,959** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,356,866.4 tonnes** estimated CO2 emissions
- **78,658,923 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4585 |
| 2 | SkyWest Airlines | 4152 |
| 3 | IndiGo | 2173 |
| 4 | EJA | 2149 |
| 5 | American Airlines | 1749 |
| 6 | Southwest Airlines | 1661 |
| 7 | ENY | 1381 |
| 8 | Delta Air Lines | 1311 |
| 9 | Lufthansa | 1255 |
| 10 | Vueling | 1020 |
| 11 | LATAM Airlines | 980 |
| 12 | WIF | 978 |
| 13 | AXM | 933 |
| 14 | AZU | 919 |
| 15 | LXJ | 850 |
| 16 | Swiss International | 795 |
| 17 | All Nippon Airways | 769 |
| 18 | Alaska Airlines | 754 |
| 19 | QLK | 726 |
| 20 | easyJet | 714 |
| 21 | EJU | 706 |
| 22 | Cathay Pacific | 658 |
| 23 | AEE | 628 |
| 24 | VIV | 623 |
| 25 | Air France | 621 |
| 26 | United Airlines | 616 |
| 27 | MXY | 593 |
| 28 | CXK | 579 |
| 29 | AXB | 546 |
| 30 | GLO | 544 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 93405 |
| 2 | 🇪🇸 ES | 7614 |
| 3 | 🇮🇳 IN | 6852 |
| 4 | 🇦🇺 AU | 6575 |
| 5 | 🇧🇷 BR | 6132 |
| 6 | 🇮🇹 IT | 5980 |
| 7 | 🇩🇪 DE | 5939 |
| 8 | 🇨🇦 CA | 5827 |
| 9 | 🇯🇵 JP | 5015 |
| 10 | 🇬🇧 GB | 4754 |
| 11 | 🇫🇷 FR | 4436 |
| 12 | 🇨🇴 CO | 3775 |
| 13 | 🇲🇽 MX | 3294 |
| 14 | 🇬🇷 GR | 3157 |
| 15 | 🇳🇴 NO | 3069 |
| 16 | 🇨🇭 CH | 2834 |
| 17 | 🇲🇾 MY | 2410 |
| 18 | 🇹🇷 TR | 2202 |
| 19 | 🇿🇦 ZA | 1887 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1826 |
| 22 | 🇵🇱 PL | 1822 |
| 23 | 🇳🇿 NZ | 1815 |
| 24 | 🇵🇭 PH | 1613 |
| 25 | 🇬🇹 GT | 1586 |
| 26 | 🇲🇦 MA | 1221 |
| 27 | 🇲🇴 MO | 1150 |
| 28 | 🇲🇪 ME | 1087 |
| 29 | 🇳🇱 NL | 1084 |
| 30 | 🇭🇷 HR | 965 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2366 |
| 2 | Denver International Airport |  | US | 1884 |
| 3 | Tokyo International Airport |  | JP | 1661 |
| 4 | Indira Gandhi International Airport |  | IN | 1491 |
| 5 | Guaymaral Airport |  | CO | 1405 |
| 6 | Harry Reid International Airport |  | US | 1400 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1380 |
| 8 | Zurich Airport |  | CH | 1246 |
| 9 | Frankfurt am Main International Airport |  | DE | 1229 |
| 10 | La Aurora Airport |  | GT | 1220 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1193 |
| 12 | Macau International Airport |  | MO | 1150 |
| 13 | El Dorado International Airport |  | CO | 1135 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1112 |
| 15 | Chicago O'Hare International Airport |  | US | 1102 |
| 16 | Madrid Barajas International Airport |  | ES | 969 |
| 17 | Capua Airport |  | IT | 963 |
| 18 | Kuala Lumpur International Airport |  | MY | 940 |
| 19 | Salt Lake City International Airport |  | US | 939 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 934 |
| 21 | Charlotte/Douglas International Airport |  | US | 854 |
| 22 | Congonhas Airport |  | BR | 854 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Charles de Gaulle International Airport |  | FR | 832 |
| 25 | Bengaluru International Airport |  | IN | 828 |
| 26 | Malpensa International Airport |  | IT | 810 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 756 |
| 28 | Ninoy Aquino International Airport |  | PH | 743 |
| 29 | Daniel K Inouye International Airport |  | US | 736 |
| 30 | Tenerife Norte Airport |  | ES | 731 |
| 31 | Barcelona International Airport |  | ES | 727 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 726 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 710 |
| 34 | Don Mueang International Airport |  | TH | 667 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 659 |
| 37 | Calgary International Airport |  | CA | 656 |
| 38 | Seattle-Tacoma International Airport |  | US | 639 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 637 |
| 40 | Viracopos International Airport |  | BR | 627 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 583 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 404 | 21m | 244 km | 1,701.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 286 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 271 | 1h 25m | 910 km | 4,252.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 260 | 1h 10m | 770 km | 3,453.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 221 | 26m | 275 km | 1,047.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 165 | 20m | 99 km | 282.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 161 | 27m | 215 km | 596.3 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 157 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 153 | 27m | 152 km | 399.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 150 | 31m | 369 km | 954.8 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 140 | 44m | 241 km | 581.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 124 | 1h 2m | 611 km | 1,307.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N915AC |  | Arthur Dunn Air Park (KX21) | Orlando Executive Airport (KORL) | 2026-06-14 22:27 UTC | 2026-06-14 22:42 UTC | 14m |
| N199SP |  | Chicago Executive Airport (KPWK) | Lake In The Hills Airport (K3CK) | 2026-06-14 22:16 UTC | 2026-06-14 22:31 UTC | 14m |
| YGA | YGA | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-06-14 22:00 UTC | 2026-06-14 22:29 UTC | 29m |
| N229MT |  | Davis Monthan Afb Airport (KDMA) | Davis Monthan Afb Airport (KDMA) | 2026-06-14 22:23 UTC | 2026-06-14 22:26 UTC | 3m |
| N4357F |  | Henderson Executive Airport (KHND) | Henderson Executive Airport (KHND) | 2026-06-14 22:21 UTC | 2026-06-14 22:22 UTC | 0m |
| SBI3750 | SBI | Istanbul Airport (LTFM) | Tunoshna Airport (UUDL) | 2026-06-14 15:54 UTC | 2026-06-14 22:19 UTC | 6h 25m |
| N65DJ |  | Linden Airport (KLDJ) | Teterboro Airport (KTEB) | 2026-06-14 22:03 UTC | 2026-06-14 22:19 UTC | 15m |
| N884CF |  | St Louis Lambert International Airport (KSTL) | Boeing Field/King County International Airport (KBFI) | 2026-06-14 18:29 UTC | 2026-06-14 22:18 UTC | 3h 49m |
| ELY364 | ELY | Vienna International Airport (LOWW) | Queen Alia International Airport (OJAI) | 2026-06-14 20:01 UTC | 2026-06-14 22:17 UTC | 2h 16m |
| ASA579 | Alaska Airlines | Chicago O'Hare International Airport (KORD) | Seattle-Tacoma International Airport (KSEA) | 2026-06-14 18:18 UTC | 2026-06-14 22:17 UTC | 3h 58m |
| N757RK |  | Georgetown Executive Airport (KGTU) | Dimmitt Municipal Airport (KT55) | 2026-06-14 20:49 UTC | 2026-06-14 22:15 UTC | 1h 26m |
| N632BL |  | Phoenix Sky Harbor International Airport (KPHX) | Santa Barbara Municipal Airport (KSBA) | 2026-06-14 21:09 UTC | 2026-06-14 22:12 UTC | 1h 3m |
| N510PR |  | Talkeetna Airport (PATK) | Mc Kinley Country Airport (81AK) | 2026-06-14 21:28 UTC | 2026-06-14 22:06 UTC | 38m |
| OUA22 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Hickory Hills Airport (10OK) | 2026-06-14 21:22 UTC | 2026-06-14 22:05 UTC | 42m |
| N739BZ |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Pine Bluffs Municipal Airport (K82V) | 2026-06-14 21:40 UTC | 2026-06-14 22:04 UTC | 24m |
| SKW5851 | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | Cedar Island Airport (WI10) | 2026-06-14 21:10 UTC | 2026-06-14 22:02 UTC | 52m |
| N61NG |  | Palo Alto Airport (KPAO) | Mc Clellan Airfield (KMCC) | 2026-06-14 21:40 UTC | 2026-06-14 22:02 UTC | 21m |
| EJT | EJT | Sydney Bankstown Airport (YSBK) | Cudal Airport (YCUA) | 2026-06-14 21:38 UTC | 2026-06-14 22:00 UTC | 22m |
| FTO388 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-06-14 21:23 UTC | 2026-06-14 21:59 UTC | 36m |
| VIV9396 | VIV | Santa Lucia Air Force Base (MMSM) | Plan De Guadalupe International Airport (MMIO) | 2026-06-14 20:56 UTC | 2026-06-14 21:57 UTC | 1h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
