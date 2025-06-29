import { createSearchParamsCache, parseAsInteger } from "nuqs/server";
import { getFiltersStateParser, getSortingStateParser } from "~/lib/parsers";
import type { Car } from "~/types/car";

export const searchParamsCache = createSearchParamsCache({
  page: parseAsInteger.withDefault(1),
  perPage: parseAsInteger.withDefault(10),
  sort: getSortingStateParser<Car>().withDefault([]),
  filters: getFiltersStateParser().withDefault([]),
});
