"use client";

import { useState, useEffect, useMemo } from "react";
import { 
  ChevronDown, 
  ChevronUp, 
  MoreHorizontal,
  Edit,
  Trash,
  Info,
  ChevronLeft,
  ChevronRight
} from "lucide-react";
import { Car, CarTableColumn } from "~/types/car";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "~/components/ui/table";
import { Button } from "~/components/ui/button";
import { 
  DropdownMenu, 
  DropdownMenuContent, 
  DropdownMenuItem, 
  DropdownMenuTrigger 
} from "~/components/ui/dropdown-menu";
import { DEFAULT_COLUMNS } from "~/hooks/cars/use-car-table-settings";
import { getCountryName } from "~/api/registries";

interface TablePaginationProps {
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}

function TablePagination({
  currentPage,
  totalPages,
  onPageChange
}: TablePaginationProps) {
  if (totalPages <= 1) return null;

  const getPageButtons = () => {
    if (totalPages <= 7) {
      return Array.from({ length: totalPages }, (_, i) => i + 1);
    }

    const buttons = [];
    
    buttons.push(1);
    
    if (currentPage > 3) {
      buttons.push('ellipsis-start');
    }

    const startPage = Math.max(2, currentPage - 1);
    const endPage = Math.min(totalPages - 1, currentPage + 1);
    
    for (let i = startPage; i <= endPage; i++) {
      buttons.push(i);
    }
    
    if (currentPage < totalPages - 2) {
      buttons.push('ellipsis-end');
    }
    
    buttons.push(totalPages);
    
    return buttons;
  };
  
  const pageButtons = getPageButtons();
  
  return (
    <div className="flex items-center justify-center gap-2 py-4">
      <Button 
        variant="default"
        size="icon" 
        onClick={() => onPageChange(currentPage - 1)}
        disabled={currentPage === 1}
        className="h-8 w-8 disabled:opacity-60 disabled:bg-muted disabled:text-muted-foreground"
      >
        <ChevronLeft className="h-4 w-4" />
      </Button>
      
      {pageButtons.map((page, index) => {
        if (page === 'ellipsis-start' || page === 'ellipsis-end') {
          return (
            <Button
              key={`ellipsis-${index}`}
              variant="outline"
              size="icon"
              disabled
              className="h-8 w-8"
            >
              ...
            </Button>
          );
        }
        
        return (
          <Button
            key={page}
            variant={currentPage === page ? "default" : "outline"}
            size="sm"
            onClick={() => onPageChange(page as number)}
            className={`h-8 w-8 hover:bg-primary hover:text-primary-foreground ${currentPage === page ? "pointer-events-none" : ""}`}
            disabled={currentPage === page}
          >
            {page}
          </Button>
        );
      })}
      
      <Button 
        variant="default"
        size="icon" 
        onClick={() => onPageChange(currentPage + 1)}
        disabled={currentPage === totalPages}
        className="h-8 w-8 disabled:opacity-60 disabled:bg-muted disabled:text-muted-foreground"
      >
        <ChevronRight className="h-4 w-4" />
      </Button>
    </div>
  );
}

interface CarTableProps {
  cars?: Car[];
  onCarSelect?: (car: Car) => void;
  onDelete?: (carId: string) => void;
  onEdit?: (car: Car) => void;
  visibleColumns?: CarTableColumn[];
  pageSize?: number;
}

export function Cars({
  cars = [],
  onCarSelect, 
  onDelete,
  onEdit,
  visibleColumns = DEFAULT_COLUMNS,
  pageSize = 10
}: CarTableProps) {
  const [sortField, setSortField] = useState<keyof Car | null>(null);
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');
  const [selectedCar, setSelectedCar] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState(1);

  const columns = visibleColumns.filter(column => column.visible);

  const handleSort = (field: keyof Car) => {
    if (sortField === field) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortField(field);
      setSortDirection('asc');
    }
  };

  const sortedCars = useMemo(() => {
    return [...cars].sort((a, b) => {
      if (!sortField) return 0;
      
      const aValue = a[sortField];
      const bValue = b[sortField];
      
      if (aValue === null || aValue === undefined) return sortDirection === 'asc' ? 1 : -1;
      if (bValue === null || bValue === undefined) return sortDirection === 'asc' ? -1 : 1;
      
      if (typeof aValue === 'object' && 'name' in aValue) {
        const aName = (aValue as any).name;
        const bName = (bValue as any).name;
        return sortDirection === 'asc' 
          ? aName.localeCompare(bName) 
          : bName.localeCompare(aName);
      }
      
      if (typeof aValue === 'string' && typeof bValue === 'string') {
        return sortDirection === 'asc' 
          ? aValue.localeCompare(bValue) 
          : bValue.localeCompare(aValue);
      }
      
      if (aValue !== undefined && bValue !== undefined) {
        return sortDirection === 'asc' 
          ? (aValue < bValue ? -1 : 1) 
          : (bValue < aValue ? -1 : 1);
      }
      
      return 0;
    });
  }, [cars, sortField, sortDirection]);

  const totalPages = Math.ceil(sortedCars.length / pageSize);
  const paginatedCars = useMemo(() => {
    const startIndex = (currentPage - 1) * pageSize;
    return sortedCars.slice(startIndex, startIndex + pageSize);
  }, [sortedCars, currentPage, pageSize]);

  useEffect(() => {
    setCurrentPage(1);
  }, [cars.length, sortField, sortDirection]);

  const handleRowClick = (car: Car) => {
    setSelectedCar(car.id);
    if (onCarSelect) {
      onCarSelect(car);
    }
  };
  
  const handlePageChange = (page: number) => {
    setCurrentPage(page);
  };

  return (
    <div className="space-y-4">
      <Table className="w-full caption-bottom text-sm">
        <TableHeader className="border-b bg-muted/50">
          <TableRow className="border-b transition-colors hover:bg-muted/50">
            {columns.map((column) => (
              <TableHead 
                key={column.key}
                onClick={() => column.key !== 'actions' && handleSort(column.key as keyof Car)}
                className={`h-12 px-4 text-left align-middle font-medium text-muted-foreground ${column.key !== 'actions' ? "cursor-pointer select-none" : ""}`}
              >
                <div className="flex items-center">
                  {column.title}
                  {sortField === column.key && (
                    <span className="ml-1">
                      {sortDirection === 'asc' ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                    </span>
                  )}
                </div>
              </TableHead>
            ))}
          </TableRow>
        </TableHeader>
        <TableBody className="[&_tr:last-child]:border-0">
          {paginatedCars.map((car) => (
            <TableRow 
              key={car.id} 
              onClick={() => handleRowClick(car)}
              className={`border-b transition-colors cursor-pointer ${selectedCar === car.id ? "bg-muted" : "hover:bg-muted/50"}`}
            >
              {columns.map((column) => {
                if (column.key === 'actions') {
                  return (
                    <TableCell key={column.key} className="p-4 align-middle text-left">
                      <DropdownMenu>
                        <DropdownMenuTrigger asChild>
                          <Button variant="ghost" className="h-8 w-8 p-0">
                            <span className="sr-only">Меню</span>
                            <MoreHorizontal className="h-4 w-4" />
                          </Button>
                        </DropdownMenuTrigger>
                        <DropdownMenuContent align="end">
                          <DropdownMenuItem 
                            onClick={(e) => {
                              e.stopPropagation();
                              onCarSelect && onCarSelect(car);
                            }}
                          >
                            <Info className="mr-2 h-4 w-4" />
                            <span>Детали</span>
                          </DropdownMenuItem>
                          <DropdownMenuItem
                            onClick={(e) => {
                              e.stopPropagation();
                              onEdit && onEdit(car);
                            }}
                          >
                            <Edit className="mr-2 h-4 w-4" />
                            <span>Редактировать</span>
                          </DropdownMenuItem>
                          <DropdownMenuItem
                            onClick={(e) => {
                              e.stopPropagation();
                              onDelete && onDelete(car.id);
                            }}
                          >
                            <Trash className="mr-2 h-4 w-4" />
                            <span>Удалить</span>
                          </DropdownMenuItem>
                        </DropdownMenuContent>
                      </DropdownMenu>
                    </TableCell>
                  );
                }
                if (column.key === 'color') {
                  return (
                    <TableCell key={column.key} className="p-4 align-middle">
                      {car.color ? (
                        <div className="flex items-center">
                          <div 
                            className="w-4 h-4 rounded-full border border-gray-300 mr-2" 
                            style={{ backgroundColor: car.color.hex_code }}
                          />
                          <span>{car.color.name}</span>
                        </div>
                      ) : (
                        <span className="text-muted-foreground">Не указан</span>
                      )}
                    </TableCell>
                  );
                }
                if (column.key === 'client') {
                  return (
                    <TableCell key={column.key} className="p-4 align-middle">
                      {car.client ? (
                        <span>{car.client.last_name} {car.client.first_name}</span>
                      ) : (
                        <span className="text-muted-foreground">Не указан</span>
                      )}
                    </TableCell>
                  );
                }
                if (column.key === 'license_plate_region') {
                  return (
                    <TableCell key={column.key} className="p-4 align-middle">
                      {car.license_plate_region ? (
                        <span>
                          {getCountryName(car.license_plate_region)}
                        </span>
                      ) : (
                        <span className="text-muted-foreground">Не указана</span>
                      )}
                    </TableCell>
                  );
                }
                return (
                  <TableCell key={column.key} className="p-4 align-middle">
                    {typeof car[column.key as keyof Car] === 'object' 
                      ? '-' 
                      : car[column.key as keyof Car]?.toString() || '-'}
                  </TableCell>
                );
              })}
            </TableRow>
          ))}
        </TableBody>
      </Table>
      
      {totalPages > 1 && (
        <>
          <div className="border-t w-full"></div>
          <div className="pb-4 flex justify-center">
            <TablePagination 
              currentPage={currentPage} 
              totalPages={totalPages} 
              onPageChange={handlePageChange} 
            />
          </div>
        </>
      )}
    </div>
  );
} 