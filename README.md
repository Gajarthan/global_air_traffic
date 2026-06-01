# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_23:26:18_UTC-green)

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

**Latest saved flight:** 2026-06-01 23:26:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-01 23:26:18 UTC

- **100,581** saved flights
- **35,706** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **100,581** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,232,183.9 tonnes** estimated CO2 emissions
- **71,430,950 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4158 |
| 2 | SkyWest Airlines | 3776 |
| 3 | IndiGo | 2027 |
| 4 | EJA | 1921 |
| 5 | American Airlines | 1630 |
| 6 | Southwest Airlines | 1522 |
| 7 | ENY | 1257 |
| 8 | Delta Air Lines | 1182 |
| 9 | Lufthansa | 1176 |
| 10 | Vueling | 941 |
| 11 | LATAM Airlines | 897 |
| 12 | WIF | 879 |
| 13 | AXM | 864 |
| 14 | AZU | 811 |
| 15 | LXJ | 761 |
| 16 | Swiss International | 732 |
| 17 | All Nippon Airways | 715 |
| 18 | Alaska Airlines | 703 |
| 19 | QLK | 677 |
| 20 | easyJet | 655 |
| 21 | EJU | 633 |
| 22 | Cathay Pacific | 605 |
| 23 | AEE | 588 |
| 24 | Air France | 581 |
| 25 | VIV | 581 |
| 26 | United Airlines | 565 |
| 27 | CXK | 541 |
| 28 | MXY | 538 |
| 29 | Japan Airlines | 506 |
| 30 | AXB | 497 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 84311 |
| 2 | 🇪🇸 ES | 6964 |
| 3 | 🇮🇳 IN | 6401 |
| 4 | 🇦🇺 AU | 6082 |
| 5 | 🇧🇷 BR | 5506 |
| 6 | 🇩🇪 DE | 5445 |
| 7 | 🇮🇹 IT | 5363 |
| 8 | 🇨🇦 CA | 5181 |
| 9 | 🇯🇵 JP | 4665 |
| 10 | 🇬🇧 GB | 4279 |
| 11 | 🇫🇷 FR | 4018 |
| 12 | 🇨🇴 CO | 3493 |
| 13 | 🇲🇽 MX | 3047 |
| 14 | 🇬🇷 GR | 2870 |
| 15 | 🇳🇴 NO | 2786 |
| 16 | 🇨🇭 CH | 2597 |
| 17 | 🇲🇾 MY | 2198 |
| 18 | 🇹🇷 TR | 1909 |
| 19 | 🇿🇦 ZA | 1753 |
| 20 | 🇳🇿 NZ | 1689 |
| 21 | 🇹🇭 TH | 1665 |
| 22 | 🇰🇷 KR | 1627 |
| 23 | 🇵🇱 PL | 1617 |
| 24 | 🇬🇹 GT | 1489 |
| 25 | 🇵🇭 PH | 1467 |
| 26 | 🇲🇦 MA | 1129 |
| 27 | 🇲🇴 MO | 1066 |
| 28 | 🇳🇱 NL | 1003 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 889 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2198 |
| 2 | Denver International Airport |  | US | 1723 |
| 3 | Tokyo International Airport |  | JP | 1547 |
| 4 | Indira Gandhi International Airport |  | IN | 1392 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1294 |
| 6 | Harry Reid International Airport |  | US | 1285 |
| 7 | Guaymaral Airport |  | CO | 1260 |
| 8 | Frankfurt am Main International Airport |  | DE | 1180 |
| 9 | Zurich Airport |  | CH | 1151 |
| 10 | La Aurora Airport |  | GT | 1145 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1089 |
| 12 | El Dorado International Airport |  | CO | 1074 |
| 13 | Macau International Airport |  | MO | 1066 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1020 |
| 15 | Chicago O'Hare International Airport |  | US | 1011 |
| 16 | Madrid Barajas International Airport |  | ES | 875 |
| 17 | Kuala Lumpur International Airport |  | MY | 869 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 866 |
| 19 | Salt Lake City International Airport |  | US | 851 |
| 20 | Capua Airport |  | IT | 832 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 783 |
| 22 | Charlotte/Douglas International Airport |  | US | 783 |
| 23 | Charles de Gaulle International Airport |  | FR | 772 |
| 24 | Malpensa International Airport |  | IT | 767 |
| 25 | Bengaluru International Airport |  | IN | 767 |
| 26 | Congonhas Airport |  | BR | 766 |
| 27 | Daniel K Inouye International Airport |  | US | 695 |
| 28 | Tenerife Norte Airport |  | ES | 692 |
| 29 | Ninoy Aquino International Airport |  | PH | 670 |
| 30 | Barcelona International Airport |  | ES | 666 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 657 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 656 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 643 |
| 34 | Amsterdam Airport Schiphol |  | NL | 619 |
| 35 | Vitoria/Foronda Airport |  | ES | 611 |
| 36 | Don Mueang International Airport |  | TH | 609 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 589 |
| 39 | Seattle-Tacoma International Airport |  | US | 579 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 519 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 365 | 21m | 244 km | 1,536.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 269 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 264 | 24m | 225 km | 1,024.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 246 | 1h 26m | 910 km | 3,860.3 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 229 | 1h 10m | 770 km | 3,042.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 156 | 20m | 99 km | 267.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 146 | 22m | 55 km | 138.8 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 141 | 31m | 369 km | 897.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 132 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 127 | 1h 39m | 1,156 km | 2,533.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 126 | 1h 1m | 695 km | 1,510.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N662JJ |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-06-01 22:58 UTC | 2026-06-01 23:26 UTC | 27m |
| N614AR |  | Grand Junction Regional Airport (KGJT) | Pinyon Airport (CO43) | 2026-06-01 22:55 UTC | 2026-06-01 23:20 UTC | 24m |
| N4RT |  | Minden-Tahoe Airport (KMEV) | Dayton Valley Airpark (KA34) | 2026-06-01 22:50 UTC | 2026-06-01 23:14 UTC | 24m |
| ANA94 | All Nippon Airways | Kansai International Airport (RJBB) | Tokyo International Airport (RJTT) | 2026-06-01 22:21 UTC | 2026-06-01 23:14 UTC | 52m |
| NBI | NBI | Gympie Airport (YGYM) | Hervey Bay Airport (YHBA) | 2026-06-01 22:46 UTC | 2026-06-01 23:14 UTC | 27m |
| N709KA |  | 80WA (80WA) | Boeing Field/King County International Airport (KBFI) | 2026-06-01 22:57 UTC | 2026-06-01 23:13 UTC | 15m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-06-01 11:47 UTC | 2026-06-01 23:03 UTC | 11h 15m |
| N699SU |  | Aurora State Airport (KUAO) | Western Helicopter Services Airport (OR38) | 2026-06-01 22:57 UTC | 2026-06-01 23:02 UTC | 5m |
| BRG671 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-06-01 22:28 UTC | 2026-06-01 23:01 UTC | 32m |
| N905LB |  | Truckee-Tahoe Airport (KTRK) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-01 22:18 UTC | 2026-06-01 22:57 UTC | 38m |
| SMASH31 | SMA | Anacacho Ranch Airport (0XS7) | Hughes Ranch Airport (50XS) | 2026-06-01 17:29 UTC | 2026-06-01 22:55 UTC | 5h 26m |
| N315EX |  | Charleston Afb/International Airport (KCHS) | L.F. Wade International International Airport (TXKF) | 2026-06-01 21:05 UTC | 2026-06-01 22:48 UTC | 1h 42m |
| N78ER |  | Fairview Airport (3MD4) | Ocean City Municipal Airport (KOXB) | 2026-06-01 21:45 UTC | 2026-06-01 22:46 UTC | 1h 1m |
| N394US |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-06-01 22:30 UTC | 2026-06-01 22:46 UTC | 15m |
| N578KA |  | Coleman A Young Municipal Airport (KDET) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-06-01 21:50 UTC | 2026-06-01 22:43 UTC | 53m |
| N69F |  | John F Kennedy International Airport (KJFK) | Teterboro Airport (KTEB) | 2026-06-01 22:06 UTC | 2026-06-01 22:43 UTC | 37m |
| N50KA |  | Roche Harbor Airport (WA09) | Boeing Field/King County International Airport (KBFI) | 2026-06-01 22:07 UTC | 2026-06-01 22:43 UTC | 35m |
| SKW5312 | SkyWest Airlines | San Francisco International Airport (KSFO) | Palm Springs International Airport (KPSP) | 2026-06-01 21:41 UTC | 2026-06-01 22:41 UTC | 59m |
| AAL2424 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-06-01 21:22 UTC | 2026-06-01 22:40 UTC | 1h 18m |
| NIT264 | NIT | Heart Of Georgia Regional Airport (KEZM) | W H 'Bud' Barron Airport (KDBN) | 2026-06-01 22:21 UTC | 2026-06-01 22:38 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
