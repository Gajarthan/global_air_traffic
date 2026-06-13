# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_12:54:15_UTC-green)

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

**Latest saved flight:** 2026-06-13 12:54:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-13 12:54:15 UTC

- **109,182** saved flights
- **38,179** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **109,182** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,335,219.2 tonnes** estimated CO2 emissions
- **77,404,015 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4494 |
| 2 | SkyWest Airlines | 4081 |
| 3 | IndiGo | 2159 |
| 4 | EJA | 2101 |
| 5 | American Airlines | 1726 |
| 6 | Southwest Airlines | 1635 |
| 7 | ENY | 1356 |
| 8 | Delta Air Lines | 1291 |
| 9 | Lufthansa | 1238 |
| 10 | Vueling | 1002 |
| 11 | LATAM Airlines | 968 |
| 12 | WIF | 960 |
| 13 | AXM | 928 |
| 14 | AZU | 898 |
| 15 | LXJ | 826 |
| 16 | Swiss International | 791 |
| 17 | All Nippon Airways | 760 |
| 18 | Alaska Airlines | 744 |
| 19 | QLK | 723 |
| 20 | easyJet | 704 |
| 21 | EJU | 696 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 622 |
| 24 | Air France | 618 |
| 25 | VIV | 618 |
| 26 | United Airlines | 603 |
| 27 | MXY | 585 |
| 28 | CXK | 573 |
| 29 | AXB | 539 |
| 30 | Japan Airlines | 537 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 91798 |
| 2 | 🇪🇸 ES | 7503 |
| 3 | 🇮🇳 IN | 6807 |
| 4 | 🇦🇺 AU | 6520 |
| 5 | 🇧🇷 BR | 6020 |
| 6 | 🇩🇪 DE | 5859 |
| 7 | 🇮🇹 IT | 5836 |
| 8 | 🇨🇦 CA | 5721 |
| 9 | 🇯🇵 JP | 4967 |
| 10 | 🇬🇧 GB | 4647 |
| 11 | 🇫🇷 FR | 4357 |
| 12 | 🇨🇴 CO | 3755 |
| 13 | 🇲🇽 MX | 3264 |
| 14 | 🇬🇷 GR | 3103 |
| 15 | 🇳🇴 NO | 3022 |
| 16 | 🇨🇭 CH | 2795 |
| 17 | 🇲🇾 MY | 2384 |
| 18 | 🇹🇷 TR | 2144 |
| 19 | 🇿🇦 ZA | 1871 |
| 20 | 🇰🇷 KR | 1828 |
| 21 | 🇹🇭 TH | 1802 |
| 22 | 🇳🇿 NZ | 1796 |
| 23 | 🇵🇱 PL | 1795 |
| 24 | 🇵🇭 PH | 1597 |
| 25 | 🇬🇹 GT | 1566 |
| 26 | 🇲🇦 MA | 1201 |
| 27 | 🇲🇴 MO | 1148 |
| 28 | 🇳🇱 NL | 1074 |
| 29 | 🇲🇪 ME | 1060 |
| 30 | 🇭🇷 HR | 954 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2342 |
| 2 | Denver International Airport |  | US | 1843 |
| 3 | Tokyo International Airport |  | JP | 1646 |
| 4 | Indira Gandhi International Airport |  | IN | 1479 |
| 5 | Guaymaral Airport |  | CO | 1390 |
| 6 | Harry Reid International Airport |  | US | 1387 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1366 |
| 8 | Zurich Airport |  | CH | 1236 |
| 9 | Frankfurt am Main International Airport |  | DE | 1219 |
| 10 | La Aurora Airport |  | GT | 1205 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1168 |
| 12 | Macau International Airport |  | MO | 1148 |
| 13 | El Dorado International Airport |  | CO | 1133 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1092 |
| 15 | Chicago O'Hare International Airport |  | US | 1084 |
| 16 | Madrid Barajas International Airport |  | ES | 950 |
| 17 | Capua Airport |  | IT | 936 |
| 18 | Kuala Lumpur International Airport |  | MY | 935 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 925 |
| 20 | Salt Lake City International Airport |  | US | 923 |
| 21 | Charlotte/Douglas International Airport |  | US | 843 |
| 22 | Congonhas Airport |  | BR | 833 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 830 |
| 24 | Charles de Gaulle International Airport |  | FR | 824 |
| 25 | Bengaluru International Airport |  | IN | 823 |
| 26 | Malpensa International Airport |  | IT | 800 |
| 27 | Ninoy Aquino International Airport |  | PH | 734 |
| 28 | Daniel K Inouye International Airport |  | US | 731 |
| 29 | Tenerife Norte Airport |  | ES | 728 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 720 |
| 31 | Barcelona International Airport |  | ES | 718 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 711 |
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
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 576 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 399 | 21m | 244 km | 1,680.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 292 | 24m | 225 km | 1,132.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 283 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 266 | 1h 25m | 910 km | 4,174.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 256 | 1h 10m | 770 km | 3,400.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 218 | 26m | 275 km | 1,033.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 152 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 148 | 31m | 369 km | 942.1 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 142 | 18m | 144 km | 353.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
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
| SMGLR | SMG | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-06-13 12:37 UTC | 2026-06-13 12:54 UTC | 17m |
| N238AM |  | Searchlight Airport (K1L3) | Harry Reid International Airport (KLAS) | 2026-06-13 12:34 UTC | 2026-06-13 12:50 UTC | 15m |
| UPS5771 | UPS | George Bush Intcntl/Houston Airport (KIAH) | Dallas-Fort Worth International Airport (KDFW) | 2026-06-13 12:03 UTC | 2026-06-13 12:45 UTC | 41m |
| TKJ6MP | TKJ | Sabiha Gokcen International Airport (LTFJ) | Sarajevo International Airport (LQSA) | 2026-06-13 11:06 UTC | 2026-06-13 12:37 UTC | 1h 31m |
| JBU716 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-13 12:31 UTC | 2026-06-13 12:31 UTC | 0m |
| DRAGO66 | DRA | Mont Louis La Quillane Airport (LFNQ) | Aerodrom dels Pirineus-Alt Urgell Airport (LESU) | 2026-06-13 12:00 UTC | 2026-06-13 12:31 UTC | 30m |
| HBZVQ | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-06-13 12:18 UTC | 2026-06-13 12:30 UTC | 12m |
| N969YC |  | Westchester County Airport (KHPN) | KHTO (KHTO) | 2026-06-13 12:03 UTC | 2026-06-13 12:30 UTC | 27m |
| TGCYE | TGC | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-06-13 12:07 UTC | 2026-06-13 12:26 UTC | 19m |
| HK5220 |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-13 11:51 UTC | 2026-06-13 12:19 UTC | 28m |
| AWH98E | AWH | Klagenfurt Airport (LOWK) | Hamburg Airport (EDDH) | 2026-06-13 10:56 UTC | 2026-06-13 12:17 UTC | 1h 21m |
| N390TC |  | Orlando Apopka Airport (KX04) | Leesburg International Airport (KLEE) | 2026-06-13 11:46 UTC | 2026-06-13 12:17 UTC | 30m |
| LOT3KL | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Pinczow Airport (EPPC) | 2026-06-13 11:43 UTC | 2026-06-13 12:10 UTC | 26m |
| VTGRB | VTG | Bharkot Airport (VI82) | Bharkot Airport (VI82) | 2026-06-13 11:59 UTC | 2026-06-13 12:10 UTC | 11m |
| N80896 |  | Denton Enterprise Airport (KDTO) | Bridgeport Municipal Airport (KXBP) | 2026-06-13 11:32 UTC | 2026-06-13 12:09 UTC | 36m |
| HBZTO | HBZ | Kagiswil Airport (LSPG) | Buochs Airport (LSZC) | 2026-06-13 11:52 UTC | 2026-06-13 12:05 UTC | 12m |
| PVD441V | PVD | London City Airport (EGLC) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-13 10:29 UTC | 2026-06-13 12:04 UTC | 1h 34m |
| DTA122 | DTA | Camembe Airport (FNCB) | Soyo Airport (FNSO) | 2026-06-13 11:30 UTC | 2026-06-13 12:04 UTC | 33m |
| RYR2CW | Ryanair | Warsaw Modlin Airport (EPMO) | LBVR (LBVR) | 2026-06-13 10:44 UTC | 2026-06-13 12:01 UTC | 1h 16m |
| HBZUZ | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-06-13 11:27 UTC | 2026-06-13 12:01 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
