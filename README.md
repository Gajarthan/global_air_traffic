# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_10:26:14_UTC-green)

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

**Latest saved flight:** 2026-05-27 10:26:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-27 10:26:14 UTC

- **95,357** saved flights
- **33,580** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **95,357** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,171,598.4 tonnes** estimated CO2 emissions
- **67,918,747 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4014 |
| 2 | SkyWest Airlines | 3538 |
| 3 | IndiGo | 1982 |
| 4 | EJA | 1797 |
| 5 | American Airlines | 1444 |
| 6 | Southwest Airlines | 1387 |
| 7 | ENY | 1176 |
| 8 | Lufthansa | 1146 |
| 9 | Delta Air Lines | 1044 |
| 10 | Vueling | 908 |
| 11 | LATAM Airlines | 858 |
| 12 | AXM | 848 |
| 13 | WIF | 836 |
| 14 | AZU | 762 |
| 15 | LXJ | 721 |
| 16 | Swiss International | 712 |
| 17 | All Nippon Airways | 709 |
| 18 | QLK | 663 |
| 19 | Alaska Airlines | 662 |
| 20 | easyJet | 626 |
| 21 | EJU | 610 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 575 |
| 24 | Air France | 565 |
| 25 | VIV | 564 |
| 26 | CXK | 507 |
| 27 | MXY | 505 |
| 28 | Japan Airlines | 493 |
| 29 | AXB | 484 |
| 30 | AIQ | 462 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78649 |
| 2 | 🇪🇸 ES | 6682 |
| 3 | 🇮🇳 IN | 6255 |
| 4 | 🇦🇺 AU | 5876 |
| 5 | 🇩🇪 DE | 5236 |
| 6 | 🇧🇷 BR | 5230 |
| 7 | 🇮🇹 IT | 5172 |
| 8 | 🇨🇦 CA | 4823 |
| 9 | 🇯🇵 JP | 4584 |
| 10 | 🇬🇧 GB | 4086 |
| 11 | 🇫🇷 FR | 3874 |
| 12 | 🇨🇴 CO | 3286 |
| 13 | 🇲🇽 MX | 2926 |
| 14 | 🇬🇷 GR | 2751 |
| 15 | 🇳🇴 NO | 2665 |
| 16 | 🇨🇭 CH | 2507 |
| 17 | 🇲🇾 MY | 2152 |
| 18 | 🇹🇷 TR | 1763 |
| 19 | 🇿🇦 ZA | 1717 |
| 20 | 🇳🇿 NZ | 1632 |
| 21 | 🇹🇭 TH | 1625 |
| 22 | 🇰🇷 KR | 1580 |
| 23 | 🇵🇱 PL | 1562 |
| 24 | 🇵🇭 PH | 1444 |
| 25 | 🇬🇹 GT | 1425 |
| 26 | 🇲🇦 MA | 1088 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 964 |
| 29 | 🇲🇪 ME | 945 |
| 30 | 🇭🇷 HR | 868 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2057 |
| 2 | Denver International Airport |  | US | 1614 |
| 3 | Tokyo International Airport |  | JP | 1521 |
| 4 | Indira Gandhi International Airport |  | IN | 1355 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1262 |
| 6 | Harry Reid International Airport |  | US | 1228 |
| 7 | Frankfurt am Main International Airport |  | DE | 1157 |
| 8 | Guaymaral Airport |  | CO | 1153 |
| 9 | Zurich Airport |  | CH | 1115 |
| 10 | La Aurora Airport |  | GT | 1091 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1031 |
| 13 | El Dorado International Airport |  | CO | 1030 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 953 |
| 15 | Chicago O'Hare International Airport |  | US | 919 |
| 16 | Kuala Lumpur International Airport |  | MY | 853 |
| 17 | Madrid Barajas International Airport |  | ES | 845 |
| 18 | Salt Lake City International Airport |  | US | 802 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 801 |
| 20 | Capua Airport |  | IT | 790 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 762 |
| 22 | Malpensa International Airport |  | IT | 752 |
| 23 | Bengaluru International Airport |  | IN | 749 |
| 24 | Charles de Gaulle International Airport |  | FR | 746 |
| 25 | Congonhas Airport |  | BR | 726 |
| 26 | Charlotte/Douglas International Airport |  | US | 723 |
| 27 | Daniel K Inouye International Airport |  | US | 682 |
| 28 | Tenerife Norte Airport |  | ES | 680 |
| 29 | Ninoy Aquino International Airport |  | PH | 659 |
| 30 | Barcelona International Airport |  | ES | 641 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 640 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 618 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 612 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Don Mueang International Airport |  | TH | 593 |
| 36 | Amsterdam Airport Schiphol |  | NL | 593 |
| 37 | Vitoria/Foronda Airport |  | ES | 591 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 569 |
| 39 | Calgary International Airport |  | CA | 563 |
| 40 | O. R. Tambo International Airport |  | ZA | 545 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 473 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 352 | 21m | 244 km | 1,482.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 260 | 24m | 225 km | 1,008.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 253 | 9m | - | - |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 242 | 1h 26m | 910 km | 3,797.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 240 | 28m | 304 km | 1,258.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 221 | 1h 10m | 770 km | 2,935.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 190 | 26m | 275 km | 900.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 144 | 27m | 215 km | 533.3 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 124 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 122 | 18m | 144 km | 303.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 120 | 1h 39m | 1,156 km | 2,394.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 52m | 1,304 km | 2,587.2 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZLT | ZLT | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-27 10:01 UTC | 2026-05-27 10:26 UTC | 24m |
| N35580 |  | Mansfield Municipal Airport (K1B9) | Lebanon Municipal Airport (KLEB) | 2026-05-27 09:19 UTC | 2026-05-27 10:05 UTC | 46m |
| PPDNM | PPD | Galeao - Antonio Carlos Jobim International Airport (SBGL) | Fazenda Santa tereza Airport (SJTQ) | 2026-05-27 09:48 UTC | 2026-05-27 09:57 UTC | 9m |
| OKBIT | OKB | Letnany Airport (LKLT) | Pardubice Airport (LKPD) | 2026-05-27 09:22 UTC | 2026-05-27 09:49 UTC | 27m |
| WIF1A | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-27 08:54 UTC | 2026-05-27 09:48 UTC | 53m |
| UFX62 | UFX | RAF Woodvale (EGOW) | Blackpool International Airport (EGNH) | 2026-05-27 09:32 UTC | 2026-05-27 09:44 UTC | 12m |
| RYR98FC | Ryanair | Poznań-Ławica Airport (EPPO) | Dubrovnik Airport (LDDU) | 2026-05-27 08:14 UTC | 2026-05-27 09:44 UTC | 1h 30m |
| PRBCB | PRB | Itu Airport (SDIU) | Fazenda Barreiro Grande Airport (SDWN) | 2026-05-27 09:08 UTC | 2026-05-27 09:43 UTC | 34m |
| FHAFD | FHA | Florac Ste Enimie Airport (LFNO) | Florac Ste Enimie Airport (LFNO) | 2026-05-27 09:27 UTC | 2026-05-27 09:41 UTC | 14m |
| N968SR |  | Van Nuys Airport (KVNY) | Phoenix Sky Harbor International Airport (KPHX) | 2026-05-27 08:42 UTC | 2026-05-27 09:39 UTC | 56m |
| SEH3JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-05-27 09:09 UTC | 2026-05-27 09:35 UTC | 26m |
| DLH1JH | Lufthansa | Munich International Airport (EDDM) | Hamburg Airport (EDDH) | 2026-05-27 08:39 UTC | 2026-05-27 09:34 UTC | 55m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-05-27 09:06 UTC | 2026-05-27 09:33 UTC | 26m |
| WIF47H | WIF | Bergen Airport Flesland (ENBR) | Trondheim Airport Vaernes (ENVA) | 2026-05-27 08:40 UTC | 2026-05-27 09:33 UTC | 53m |
| TKJ7MW | TKJ | Václav Havel Airport (LKPR) | Tabor Airport (LKTA) | 2026-05-27 09:04 UTC | 2026-05-27 09:31 UTC | 27m |
| IBB47MJ | IBB | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-05-27 09:15 UTC | 2026-05-27 09:30 UTC | 15m |
| AFR34UP | Air France | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-05-27 08:12 UTC | 2026-05-27 09:30 UTC | 1h 17m |
| FGAHV | FGA | Chambery-Challes-les-Eaux Airport (LFLE) | Courchevel Airport (LFLJ) | 2026-05-27 09:03 UTC | 2026-05-27 09:26 UTC | 23m |
| NOZ52K | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-05-27 08:44 UTC | 2026-05-27 09:25 UTC | 41m |
| HHE61A | HHE | De Kooy Airport (EHKD) | Beccles Airport (EGSM) | 2026-05-27 08:51 UTC | 2026-05-27 09:25 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
