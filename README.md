# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_16:59:47_UTC-green)

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

**Latest saved flight:** 2026-05-16 16:59:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 16:59:47 UTC

- **84,944** saved flights
- **30,545** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,944** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,047,660.1 tonnes** estimated CO2 emissions
- **60,733,920 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3640 |
| 2 | SkyWest Airlines | 3133 |
| 3 | IndiGo | 1835 |
| 4 | EJA | 1598 |
| 5 | American Airlines | 1304 |
| 6 | Southwest Airlines | 1238 |
| 7 | Lufthansa | 1082 |
| 8 | ENY | 1056 |
| 9 | Delta Air Lines | 923 |
| 10 | Vueling | 806 |
| 11 | AXM | 769 |
| 12 | LATAM Airlines | 769 |
| 13 | WIF | 734 |
| 14 | AZU | 665 |
| 15 | All Nippon Airways | 659 |
| 16 | Swiss International | 659 |
| 17 | LXJ | 623 |
| 18 | QLK | 620 |
| 19 | Alaska Airlines | 600 |
| 20 | easyJet | 557 |
| 21 | EJU | 538 |
| 22 | AEE | 534 |
| 23 | Cathay Pacific | 533 |
| 24 | VIV | 508 |
| 25 | Air France | 498 |
| 26 | Japan Airlines | 474 |
| 27 | AXB | 449 |
| 28 | CXK | 449 |
| 29 | MXY | 425 |
| 30 | AIQ | 417 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69545 |
| 2 | 🇪🇸 ES | 6011 |
| 3 | 🇮🇳 IN | 5741 |
| 4 | 🇦🇺 AU | 5418 |
| 5 | 🇩🇪 DE | 4740 |
| 6 | 🇮🇹 IT | 4681 |
| 7 | 🇧🇷 BR | 4676 |
| 8 | 🇯🇵 JP | 4258 |
| 9 | 🇨🇦 CA | 4220 |
| 10 | 🇬🇧 GB | 3619 |
| 11 | 🇫🇷 FR | 3378 |
| 12 | 🇨🇴 CO | 2845 |
| 13 | 🇲🇽 MX | 2586 |
| 14 | 🇬🇷 GR | 2466 |
| 15 | 🇳🇴 NO | 2373 |
| 16 | 🇨🇭 CH | 2238 |
| 17 | 🇲🇾 MY | 1929 |
| 18 | 🇿🇦 ZA | 1600 |
| 19 | 🇹🇷 TR | 1517 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1475 |
| 22 | 🇵🇱 PL | 1412 |
| 23 | 🇵🇭 PH | 1332 |
| 24 | 🇰🇷 KR | 1312 |
| 25 | 🇬🇹 GT | 1281 |
| 26 | 🇲🇦 MA | 985 |
| 27 | 🇲🇴 MO | 983 |
| 28 | 🇲🇪 ME | 887 |
| 29 | 🇳🇱 NL | 864 |
| 30 | 🇭🇷 HR | 759 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1854 |
| 2 | Denver International Airport |  | US | 1424 |
| 3 | Tokyo International Airport |  | JP | 1423 |
| 4 | Indira Gandhi International Airport |  | IN | 1227 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1188 |
| 6 | Frankfurt am Main International Airport |  | DE | 1093 |
| 7 | Harry Reid International Airport |  | US | 1069 |
| 8 | Zurich Airport |  | CH | 1008 |
| 9 | Macau International Airport |  | MO | 983 |
| 10 | La Aurora Airport |  | GT | 971 |
| 11 | Guaymaral Airport |  | CO | 963 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 914 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 853 |
| 15 | Chicago O'Hare International Airport |  | US | 819 |
| 16 | Madrid Barajas International Airport |  | ES | 773 |
| 17 | Kuala Lumpur International Airport |  | MY | 766 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 731 |
| 19 | Malpensa International Airport |  | IT | 707 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 707 |
| 21 | Salt Lake City International Airport |  | US | 706 |
| 22 | Bengaluru International Airport |  | IN | 699 |
| 23 | Capua Airport |  | IT | 693 |
| 24 | Charles de Gaulle International Airport |  | FR | 663 |
| 25 | Charlotte/Douglas International Airport |  | US | 659 |
| 26 | Congonhas Airport |  | BR | 659 |
| 27 | Daniel K Inouye International Airport |  | US | 618 |
| 28 | Tenerife Norte Airport |  | ES | 617 |
| 29 | Ninoy Aquino International Airport |  | PH | 610 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 572 |
| 32 | Barcelona International Airport |  | ES | 569 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 568 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 549 |
| 35 | Vitoria/Foronda Airport |  | ES | 539 |
| 36 | Don Mueang International Airport |  | TH | 534 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 534 |
| 38 | Amsterdam Airport Schiphol |  | NL | 525 |
| 39 | O. R. Tambo International Airport |  | ZA | 505 |
| 40 | Calgary International Airport |  | CA | 496 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 399 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 314 | 21m | 244 km | 1,322.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 275 | 1h 7m | 706 km | 3,348.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 224 | 28m | 304 km | 1,174.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 218 | 14m | 114 km | 427.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 216 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 193 | 1h 11m | 770 km | 2,563.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 192 | 19m | 165 km | 546.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 177 | 26m | 275 km | 838.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 145 | 20m | 99 km | 248.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 133 | 31m | 369 km | 846.6 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 127 | 27m | 152 km | 331.9 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 124 | 20m | 147 km | 313.8 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 122 | 14m | 154 km | 323.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 120 | 20m | 250 km | 518.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 107 | 18m | 144 km | 266.2 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 102 | 1h 41m | 1,156 km | 2,034.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AZG786 | AZG | Frankfurt-Hahn Airport (EDFH) | Macau International Airport (VMMC) | 2026-05-16 01:17 UTC | 2026-05-16 16:59 UTC | 15h 42m |
| IFA6321 | IFA | Madrid Barajas International Airport (LEMD) | Rochester International Airport (KRST) | 2026-05-16 08:12 UTC | 2026-05-16 16:59 UTC | 8h 47m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-16 16:42 UTC | 2026-05-16 16:57 UTC | 14m |
| N3455S |  | Perdido Winds Airpark (AL08) | Perdido Winds Airpark (AL08) | 2026-05-16 16:30 UTC | 2026-05-16 16:51 UTC | 20m |
| CFPCX | CFP | Vancouver International Airport (CYVR) | Squamish Airport (CYSE) | 2026-05-16 16:28 UTC | 2026-05-16 16:50 UTC | 21m |
| N442SA |  | Greeley-Weld County Airport (KGXY) | Rocky Mountain Metro Airport (KBJC) | 2026-05-16 16:03 UTC | 2026-05-16 16:50 UTC | 47m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-16 16:20 UTC | 2026-05-16 16:41 UTC | 21m |
| TGOZI | TGO | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-05-16 15:49 UTC | 2026-05-16 16:37 UTC | 47m |
| N6141J |  | Mitchell Municipal Airport (KMHE) | Brookings Regional Airport (KBKX) | 2026-05-16 15:47 UTC | 2026-05-16 16:36 UTC | 48m |
| N440EH |  | Wiley Post Airport (KPWA) | Duke Ranch Airport (TX38) | 2026-05-16 13:55 UTC | 2026-05-16 16:34 UTC | 2h 38m |
| N41DZ |  | Arthur Dunn Air Park (KX21) | Arthur Dunn Air Park (KX21) | 2026-05-16 15:52 UTC | 2026-05-16 16:32 UTC | 39m |
| N529LF |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-05-16 15:53 UTC | 2026-05-16 16:31 UTC | 38m |
| LXJ438 | LXJ | Rainelle Airport (WV30) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-16 15:32 UTC | 2026-05-16 16:30 UTC | 57m |
| N208HF |  | Donegal Springs Airpark (KN71) | Donegal Springs Airpark (KN71) | 2026-05-16 16:08 UTC | 2026-05-16 16:29 UTC | 21m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-16 16:15 UTC | 2026-05-16 16:29 UTC | 13m |
| HK5431G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-16 16:11 UTC | 2026-05-16 16:25 UTC | 14m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-05-16 16:10 UTC | 2026-05-16 16:25 UTC | 14m |
| AUR209 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-05-16 16:07 UTC | 2026-05-16 16:20 UTC | 13m |
| ERU902 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-05-16 15:30 UTC | 2026-05-16 16:20 UTC | 50m |
| MVK77 | MVK | Mankato Regional Airport (KMKT) | Rochester International Airport (KRST) | 2026-05-16 15:18 UTC | 2026-05-16 16:20 UTC | 1h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
