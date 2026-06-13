# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_09:27:53_UTC-green)

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

**Latest saved flight:** 2026-06-13 09:27:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-13 09:27:53 UTC

- **109,069** saved flights
- **38,151** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **109,069** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,334,098.3 tonnes** estimated CO2 emissions
- **77,339,030 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4485 |
| 2 | SkyWest Airlines | 4081 |
| 3 | IndiGo | 2156 |
| 4 | EJA | 2101 |
| 5 | American Airlines | 1726 |
| 6 | Southwest Airlines | 1635 |
| 7 | ENY | 1356 |
| 8 | Delta Air Lines | 1291 |
| 9 | Lufthansa | 1238 |
| 10 | Vueling | 1001 |
| 11 | LATAM Airlines | 966 |
| 12 | WIF | 959 |
| 13 | AXM | 927 |
| 14 | AZU | 896 |
| 15 | LXJ | 826 |
| 16 | Swiss International | 791 |
| 17 | All Nippon Airways | 760 |
| 18 | Alaska Airlines | 744 |
| 19 | QLK | 723 |
| 20 | easyJet | 703 |
| 21 | EJU | 695 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 621 |
| 24 | VIV | 618 |
| 25 | Air France | 616 |
| 26 | United Airlines | 603 |
| 27 | MXY | 585 |
| 28 | CXK | 573 |
| 29 | AXB | 537 |
| 30 | Japan Airlines | 537 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 91774 |
| 2 | 🇪🇸 ES | 7496 |
| 3 | 🇮🇳 IN | 6794 |
| 4 | 🇦🇺 AU | 6520 |
| 5 | 🇧🇷 BR | 6010 |
| 6 | 🇩🇪 DE | 5853 |
| 7 | 🇮🇹 IT | 5824 |
| 8 | 🇨🇦 CA | 5721 |
| 9 | 🇯🇵 JP | 4963 |
| 10 | 🇬🇧 GB | 4635 |
| 11 | 🇫🇷 FR | 4344 |
| 12 | 🇨🇴 CO | 3750 |
| 13 | 🇲🇽 MX | 3264 |
| 14 | 🇬🇷 GR | 3096 |
| 15 | 🇳🇴 NO | 3018 |
| 16 | 🇨🇭 CH | 2785 |
| 17 | 🇲🇾 MY | 2375 |
| 18 | 🇹🇷 TR | 2138 |
| 19 | 🇿🇦 ZA | 1861 |
| 20 | 🇰🇷 KR | 1820 |
| 21 | 🇹🇭 TH | 1799 |
| 22 | 🇳🇿 NZ | 1796 |
| 23 | 🇵🇱 PL | 1788 |
| 24 | 🇵🇭 PH | 1597 |
| 25 | 🇬🇹 GT | 1564 |
| 26 | 🇲🇦 MA | 1199 |
| 27 | 🇲🇴 MO | 1148 |
| 28 | 🇳🇱 NL | 1074 |
| 29 | 🇲🇪 ME | 1056 |
| 30 | 🇭🇷 HR | 954 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2341 |
| 2 | Denver International Airport |  | US | 1843 |
| 3 | Tokyo International Airport |  | JP | 1644 |
| 4 | Indira Gandhi International Airport |  | IN | 1477 |
| 5 | Harry Reid International Airport |  | US | 1386 |
| 6 | Guaymaral Airport |  | CO | 1385 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1363 |
| 8 | Zurich Airport |  | CH | 1235 |
| 9 | Frankfurt am Main International Airport |  | DE | 1219 |
| 10 | La Aurora Airport |  | GT | 1204 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1168 |
| 12 | Macau International Airport |  | MO | 1148 |
| 13 | El Dorado International Airport |  | CO | 1133 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1092 |
| 15 | Chicago O'Hare International Airport |  | US | 1084 |
| 16 | Madrid Barajas International Airport |  | ES | 950 |
| 17 | Capua Airport |  | IT | 934 |
| 18 | Kuala Lumpur International Airport |  | MY | 931 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 925 |
| 20 | Salt Lake City International Airport |  | US | 923 |
| 21 | Charlotte/Douglas International Airport |  | US | 842 |
| 22 | Congonhas Airport |  | BR | 831 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 830 |
| 24 | Charles de Gaulle International Airport |  | FR | 823 |
| 25 | Bengaluru International Airport |  | IN | 821 |
| 26 | Malpensa International Airport |  | IT | 800 |
| 27 | Ninoy Aquino International Airport |  | PH | 734 |
| 28 | Daniel K Inouye International Airport |  | US | 731 |
| 29 | Tenerife Norte Airport |  | ES | 728 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 718 |
| 31 | Barcelona International Airport |  | ES | 717 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 708 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 701 |
| 34 | Amsterdam Airport Schiphol |  | NL | 664 |
| 35 | Don Mueang International Airport |  | TH | 657 |
| 36 | Vitoria/Foronda Airport |  | ES | 648 |
| 37 | Calgary International Airport |  | CA | 642 |
| 38 | Seattle-Tacoma International Airport |  | US | 627 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 625 |
| 40 | Viracopos International Airport |  | BR | 616 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 574 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 399 | 21m | 244 km | 1,680.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 292 | 24m | 225 km | 1,132.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 283 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 265 | 1h 25m | 910 km | 4,158.5 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 255 | 1h 10m | 770 km | 3,387.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 223 | 19m | 165 km | 634.3 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 218 | 26m | 275 km | 1,033.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 208 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 152 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 148 | 31m | 369 km | 942.1 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 142 | 18m | 144 km | 353.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 140 | 20m | 250 km | 604.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 132 | 1h 1m | 695 km | 1,582.3 t |
| 25 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 132 | 44m | 241 km | 548.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 130 | 1h 43m | 1,423 km | 3,190.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 122 | 1h 2m | 611 km | 1,286.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7160V |  | Searchlight Airport (K1L3) | Harry Reid International Airport (KLAS) | 2026-06-13 09:09 UTC | 2026-06-13 09:27 UTC | 18m |
| EZS72QV | EZS | Geneva Cointrin International Airport (LSGG) | Ajaccio-Napoleon Bonaparte Airport (LFKJ) | 2026-06-13 08:26 UTC | 2026-06-13 09:21 UTC | 55m |
| HBZUZ | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-06-13 07:41 UTC | 2026-06-13 09:11 UTC | 1h 29m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-06-12 21:49 UTC | 2026-06-13 09:09 UTC | 11h 19m |
| HBZZZ | HBZ | Wangen-Lachen Airport (LSPV) | LSMF (LSMF) | 2026-06-13 08:18 UTC | 2026-06-13 09:01 UTC | 42m |
| EIS91 | EIS | Vilnius International Airport (EYVI) | Moletai Airport (EYMO) | 2026-06-13 08:15 UTC | 2026-06-13 08:58 UTC | 43m |
| RTV2N | RTV | Vilar Da Luz Airport (LPVL) | Viseu Airport (LPVZ) | 2026-06-13 08:21 UTC | 2026-06-13 08:57 UTC | 36m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-13 08:00 UTC | 2026-06-13 08:54 UTC | 53m |
| GAWGB | GAW | Rochester Airport (EGTO) | Rochester Airport (EGTO) | 2026-06-13 08:48 UTC | 2026-06-13 08:49 UTC | 1m |
| GASTN61 | GAS | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-06-13 07:40 UTC | 2026-06-13 08:48 UTC | 1h 8m |
| OAL042 | OAL | Eleftherios Venizelos International Airport (LGAV) | Kithira Airport (LGKC) | 2026-06-13 08:15 UTC | 2026-06-13 08:45 UTC | 29m |
| AWQ176 | AWQ | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-06-13 08:21 UTC | 2026-06-13 08:34 UTC | 12m |
| AUR201 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-06-13 08:18 UTC | 2026-06-13 08:32 UTC | 13m |
| HBKLA | HBK | Lommis Airfield (LSZT) | Lommis Airfield (LSZT) | 2026-06-13 07:58 UTC | 2026-06-13 08:31 UTC | 33m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-06-13 08:09 UTC | 2026-06-13 08:30 UTC | 20m |
| HBZNH | HBZ | Zweisimmen Airport (LSTZ) | Raron Airport (LSTA) | 2026-06-13 06:56 UTC | 2026-06-13 08:28 UTC | 1h 32m |
| LLR516 | LLR | Cochin International Airport (VOCI) | Coimbatore Air Force Station (VOSX) | 2026-06-13 07:55 UTC | 2026-06-13 08:26 UTC | 31m |
| DTR69C | DTR | Pantelleria Airport (LICG) | Trapani / Birgi Airport (LICT) | 2026-06-13 08:02 UTC | 2026-06-13 08:25 UTC | 23m |
| BGA113R | BGA | Toulouse-Blagnac Airport (LFBO) | Hamburg-Finkenwerder Airport (EDHI) | 2026-06-13 06:23 UTC | 2026-06-13 08:23 UTC | 1h 59m |
| FD618 |  | Perth Jandakot Airport (YPJT) | Dongara Airport (YDRA) | 2026-06-13 07:32 UTC | 2026-06-13 08:20 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
